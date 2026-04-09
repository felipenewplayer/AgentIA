from app.core.cerebro import get_llm
from app.tool.rag_tool import buscar_contexto

llm = get_llm()

def run_agent(query: str):
    
    # Decisão simples (Depois vou evoluir)
    if "documento" in query or "texto" in query:
        contexto = buscar_contexto.invoke(query)
    else:
        contexto = ""
    
    # Criação do prompt
    prompt = f"""
    Use o contexto abaixo para responder:
    
    {contexto}

    Pergunta: {query}
    """

    #LLM responde
    resposta = llm.invoke(prompt)

    return resposta.content