from fastapi import FastAPI
from pydantic import BaseModel
import ollama
from pdfminer.high_level import extract_text
import json
import os
from pathlib import Path

app = FastAPI()

# Load PDFs into memory on startup
PDF_DIR = Path("data/ron_leavitt_legacy_stack")
documents = {}

# Load all PDFs
for pdf_file in PDF_DIR.glob("*.pdf"):
    try:
        text = extract_text(str(pdf_file))
        documents[pdf_file.stem] = text
        print(f"Loaded: {pdf_file.name}")
    except Exception as e:
        print(f"Error loading {pdf_file.name}: {e}")

# Combine all documents
full_context = "\n\n---\n\n".join([f"Document: {name}\n{text}" for name, text in documents.items()])

class AskBody(BaseModel):
    query: str

@app.post("/ask")
def ask(body: AskBody):
    # Create prompt with context
    prompt = f"""You are a family historian. Use ONLY the following family documents to answer questions.
    
Context from family documents:
{full_context[:4000]}  # Limit context size

Question: {body.query}

Answer based only on the documents above. If the information isn't in the documents, say "I don't have that information in the family records."
"""
    
    # Get response from Ollama
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return {"answer": response['message']['content']}

@app.get("/")
def root():
    return {"status": "ready", "documents_loaded": len(documents)}