from app.agent.agent import run_agent

while True:
    query = input("Você: ")
    resposta = run_agent(query)
    print("IA:", resposta)