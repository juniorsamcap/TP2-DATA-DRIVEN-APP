from fastapi import FastAPI
from langchain_community.llms import FakeListLLM
from pydantic import BaseModel

app = FastAPI(
    title="Chatbot com Fake LLM (LangChain)",
    description="API protótipo utilizando LangChain e FakeListLLM para testes rápidos.",
)

# Respostas simuladas pré-definidas para o chatbot
respostas_simuladas = [
    "Olá! Sou um chatbot de teste integrado com LangChain.",
    "Para testes de arquitetura e validação de rotas, a resposta do Fake LLM é instantânea!",
    "Esta é uma resposta simulada para validar o fluxo de dados do FastAPI.",
]

# Inicializa o FakeListLLM do LangChain
llm = FakeListLLM(responses=respostas_simuladas)


class EntradaMensagem(BaseModel):
    mensagem: str


@app.post("/chat")
def conversar(dados: EntradaMensagem):
    resposta = llm.invoke(dados.mensagem)
    return {"mensagem_usuario": dados.mensagem, "resposta_chatbot": resposta}