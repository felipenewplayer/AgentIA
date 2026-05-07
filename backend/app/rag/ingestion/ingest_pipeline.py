from app.rag.vectorstore.chroma_store import get_vector_store
from app.rag.ingestion.ingest_pipeline import ingest_pipeline
def create_embeddings():

    vector_store = get_vector_store()

    chunks = ingest_pipeline()

    vector_store.add_documents(chunks)

    return vector_store