from fastapi import FastAPI, Query
from pydantic import BaseModel
import chromadb, subprocess, tempfile, os, uuid, json
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

emb = OllamaEmbeddings(model="nomic-embed-text")
db  = Chroma(collection_name="family_vectors",
             persist_directory="chroma",
             embedding_function=emb)
llm = ChatOllama(model="llama3", temperature=0.2)

SYS = """
You are an ancestor historian.  
Use ONLY the context supplied.  
If context lacks an answer, reply: "Insufficient data."  
Return concise paragraphs, no hallucinations.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYS),
    ("human", "{question}\n\nContext:\n{context}")
])

app = FastAPI()

class AskBody(BaseModel):
    query: str

@app.post("/ask")
def ask(body: AskBody):
    docs = db.similarity_search(body.query, k=6)
    ctx  = "\n---\n".join(d.page_content for d in docs)
    answer = prompt | llm
    return {"answer": answer.invoke({"question": body.query, "context": ctx})}

@app.post("/podcast")
def podcast(body: AskBody):
    # Build 1 600-word script
    docs = db.similarity_search(body.query, k=40)
    ctx  = "\n".join(d.page_content for d in docs)
    script = llm.invoke(f"Write a 1600-word podcast transcript "
                        f"with two hosts about: {body.query}\n\nSource:\n{ctx}")
    # TTS via piper (English male voice)
    wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
    subprocess.run(["piper", "-m", "en_US-libritts-high.onnx", "-t", script, "-o", wav])
    mp3 = wav.replace(".wav", ".mp3")
    subprocess.run(["ffmpeg", "-y", "-i", wav, "-codec:a", "libmp3lame", "-b:a", "128k", mp3])
    os.remove(wav)
    return {"download": f"/audio/{os.path.basename(mp3)}"}