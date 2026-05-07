from langchain_ollama import ChatOllama
from app.tool.rag_tool import buscar_contexto
def get_llm():
   return ChatOllama(
    model="phi3",
    temperature=0.5
)
   
tools =  [buscar_contexto]
