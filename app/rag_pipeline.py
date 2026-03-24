from pypdf import PdfReader
from app.embeddings import embed
from app.vector_store import add_documents, query_documents
from app.llm import generate_answer


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text


def split_text(text, chunk_size=500, overlap=50):
    chunks = []

    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i+chunk_size])

    return chunks


def process_pdf(file_path):
    text = load_pdf(file_path)
    chunks = split_text(text)

    embeddings = embed(chunks)
    add_documents(chunks, embeddings)


def ask_question(query):
    query_embedding = embed([query])[0]

    docs = query_documents(query_embedding)

    context = "\n\n".join(docs)

    prompt = f"""
    Answer ONLY using the context below.
    If not found, say "I don't know".

    Context:
    {context}

    Question:
    {query}
    """

    return generate_answer(prompt)