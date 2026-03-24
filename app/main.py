from fastapi import FastAPI
from pydantic import BaseModel
import os

from app.rag_pipeline import ask_question, process_pdf
from app.vector_store import collection

app = FastAPI()

DATA_DIR = "data/docs"
loaded = False   # ✅ global flag


class Query(BaseModel):
    question: str


def load_data_once():
    global loaded

    if loaded or collection.count() > 0:
        return

    print("Loading documents...")

    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdf"):
            process_pdf(os.path.join(DATA_DIR, file))

    loaded = True
    print("Documents loaded ✅")


@app.get("/")
def home():
    return {"message": "RAGASHA is running 🚀"}


@app.post("/ask")
def ask(q: Query):
    load_data_once()   # ✅ load only when needed
    return {"answer": ask_question(q.question)}