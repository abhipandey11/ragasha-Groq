from fastapi import FastAPI
from pydantic import BaseModel
import os

from app.rag_pipeline import ask_question, process_pdf
from app.vector_store import collection

app = FastAPI()

DATA_DIR = "data/docs"


class Query(BaseModel):
    question: str


# ✅ Auto load documents only once
@app.on_event("startup")
def load_documents():
    if collection.count() > 0:
        print("Data already loaded ✅")
        return

    print("Loading documents...")

    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdf"):
            file_path = os.path.join(DATA_DIR, file)
            print(f"Processing: {file}")
            process_pdf(file_path)

    print("All documents loaded ✅")


@app.get("/")
def home():
    return {"message": "RAGASHA is running 🚀"}


@app.post("/ask")
def ask(q: Query):
    return {"answer": ask_question(q.question)}