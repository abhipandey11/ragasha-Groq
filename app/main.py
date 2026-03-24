from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import ask_question

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAGASHA is running 🚀"}

@app.post("/ask")
def ask(q: Query):
    return {"answer": ask_question(q.question)}