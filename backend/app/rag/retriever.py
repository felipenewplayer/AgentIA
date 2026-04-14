from app.rag.persist import create_vector_store

def get_retriever():
    vector_store = create_vector_store()
    return vector_store.as_retriever()