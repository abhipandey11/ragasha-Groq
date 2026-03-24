# 🤖 RAGASHA - Retrieval Augmented AI Assistant

RAGASHA is an AI-powered system that answers questions based on custom documents using Retrieval-Augmented Generation (RAG).

## 🚀 Features
- Ask questions from PDFs
- Fast retrieval using ChromaDB
- LLM powered by Groq (LLaMA 3)
- Streamlit UI

## 🛠 Tech Stack
- FastAPI
- ChromaDB
- Sentence Transformers
- Groq API
- Streamlit

## ▶️ Run Locally

```bash
uvicorn app.main:app --reload
streamlit run frontend/app.py
```