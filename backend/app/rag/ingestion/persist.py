from langchain_chroma import Chroma
from app.rag.embeddings.embedding_provider import get_embedding


DB_PATH = "db/chroma_db"

def get_vector_store():

    embedding = get_embedding()

    return Chroma(
        embedding_function=embedding,
        persist_directory=DB_PATH
    )