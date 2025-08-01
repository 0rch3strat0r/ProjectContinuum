import pathlib, chromadb, uuid, re
from pdfminer.high_level import extract_text
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_DIR = pathlib.Path(__file__).parent / "data" / "ron_leavitt_legacy_stack"
COLL_NAME = "family_vectors"

emb_fn   = OllamaEmbeddings(model="nomic-embed-text")
client   = chromadb.PersistentClient(path=str(pathlib.Path(__file__).parent / "chroma"))
coll     = client.get_or_create_collection(COLL_NAME, embedding_function=emb_fn)

splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=60)

def clean(txt:str)->str:
    return re.sub(r"\s+", " ", txt).strip()

def ingest_pdf(pdf_path:pathlib.Path):
    raw = extract_text(str(pdf_path))
    for chunk in splitter.split_text(raw):
        coll.add(documents=[clean(chunk)],
                 ids=[str(uuid.uuid4())],
                 metadatas=[{"source": pdf_path.name}])

if __name__ == "__main__":
    for pdf in DATA_DIR.glob("*.pdf"):
        print(f"Ingesting {pdf.name}")
        ingest_pdf(pdf)
    print("✅  Ingestion complete")