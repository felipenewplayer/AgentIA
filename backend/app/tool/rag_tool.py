from langchain_core.tools import tool
from app.rag.retriever import get_retriever

retriever = get_retriever()

@tool
def buscar_contexto(query: str) -> str:
    """Busca informações no banco vetorial"""
    docs = retriever.invoke(query)
    return "\n".join([d.page_content for d in docs])