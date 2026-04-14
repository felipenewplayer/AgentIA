from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# importa seu agent
from app.agent.agent import run_agent

app = FastAPI()

# CORS (pra Angular funcionar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# modelo da requisição
class Question(BaseModel):
    question: str

# rota principal
@app.post("/ask")
def ask(question: Question):
    response = run_agent(question.question)
    return {"response": response}

@app.get("/")
def home():
    return {"status": "ok", "message": "API rodando 🚀"}