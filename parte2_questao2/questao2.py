from fastapi import FastAPI, HTTPException
from langchain_community.llms import FakeListLLM
from pydantic import BaseModel

app = FastAPI(
    title="API de Tradução com LangChain (OpenAI Simulado)",
    description="API que simula a tradução de textos de inglês para francês utilizando LangChain para testes sem custo.",
)

# Respostas simuladas em francês para validar o fluxo de tradução
respostas_traduzidas = [
    "L'intelligence artificielle transforme le développement de logiciels.",
    "Ceci est une traduction simulée pour valider l'intégration du système.",
]

# Inicializa o modelo simulado via LangChain
llm = FakeListLLM(responses=respostas_traduzidas)


class EntradaTraducao(BaseModel):
    texto: str


@app.post("/traduzir")
def traduzir_texto(dados: EntradaTraducao):
    if not dados.texto.strip():
        raise HTTPException(status_code=400, detail="O texto não pode estar vazio.")

    try:
        # Invoca o modelo simulado via LangChain
        texto_traduzido = llm.invoke(dados.texto)

        return {
            "texto_original": dados.texto,
            "texto_traduzido": texto_traduzido,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao processar a tradução: {str(e)}"
        )