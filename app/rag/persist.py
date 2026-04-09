from langchain_chroma import Chroma
from app.rag.embedding import get_embedding
from app.rag.loader import load_and_split

def create_vector_store():
    embedding = get_embedding()
    chunks = load_and_split()

    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory="db/chroma_db"
    )

    vector_store.add_documents(chunks)

    return vector_store