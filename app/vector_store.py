import chromadb

# Persistent database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="ragasha_docs")


def add_documents(chunks, embeddings):
    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )


def query_documents(query_embedding, n_results=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]


def clear_collection():
    global collection
    try:
        client.delete_collection("ragasha_docs")
    except:
        pass

    collection = client.get_or_create_collection(name="ragasha_docs")