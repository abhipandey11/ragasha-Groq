# 🤖 RAGASHA – Retrieval Augmented AI Assistant

RAGASHA is a Retrieval-Augmented Generation (RAG) system that answers user questions based on custom PDF documents using semantic search and LLMs.

---

## 🚀 Features

* 📄 Load and process PDF documents
* 🔍 Semantic search using ChromaDB
* 🧠 LLM-powered responses (Groq API - LLaMA 3)
* ⚡ FastAPI backend
* 🌐 Streamlit frontend
* 💾 Persistent vector database (ChromaDB)

---

## 🛠 Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Vector DB:** ChromaDB
* **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **LLM:** Groq (LLaMA 3)
* **Deployment:** Railway

---

## 📁 Project Structure

```
ragasha/
│── app/
│   │── __init__.py
│   │── main.py
│   │── rag_pipeline.py
│   │── embeddings.py
│   │── vector_store.py
│   │── llm.py
│
│── data/docs/
│   │── sample.pdf
│
│── chroma_db/
│
│── frontend/
│   │── app.py
│
│── requirements.txt
│── Procfile
│── README.md
```

---

## ⚙️ Setup Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ragasha.git
cd ragasha
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add environment variable

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run backend

```
uvicorn app.main:app --reload
```

---

### 6️⃣ Run frontend

```
streamlit run frontend/app.py
```
---

## 🧠 How it Works

1. PDFs are processed into chunks
2. Chunks are converted into embeddings
3. Stored in ChromaDB
4. User query is embedded
5. Relevant chunks retrieved
6. Context passed to LLM (Groq)
7. Answer generated

---

## 👨‍💻 Author

Abhi Pandey

