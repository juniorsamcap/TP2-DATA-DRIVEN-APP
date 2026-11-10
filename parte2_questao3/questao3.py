from typing import List, Optional
from fastapi import FastAPI, HTTPException
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = FastAPI(
    title="API de Tradução (Inglês -> Alemão) com LangChain e HuggingFace",
    description="API gratuita que utiliza o modelo Helsinki-NLP/opus-mt-en-de para tradução de inglês para alemão.",
)

# 1. Carregamento direto das classes HuggingFace (Open-Source)
NOME_MODELO = "Helsinki-NLP/opus-mt-en-de"
tokenizador = AutoTokenizer.from_pretrained(NOME_MODELO)
modelo = AutoModelForSeq2SeqLM.from_pretrained(NOME_MODELO)


# 2. Classe Customizada LangChain para evitar limitações da pipeline depreciada
class TradutorHuggingFaceLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "huggingface_seq2seq"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs,
    ) -> str:
        inputs = tokenizador(
            prompt, return_tensors="pt", padding=True, truncation=True
        )
        outputs = modelo.generate(**inputs, max_new_tokens=256)
        traducao = tokenizador.decode(outputs[0], skip_special_tokens=True)
        return traducao


# 3. Inicialização da LLM via LangChain
llm = TradutorHuggingFaceLLM()


class EntradaTraducao(BaseModel):
    texto: str


@app.post("/traduzir")
def traduzir_texto(dados: EntradaTraducao):
    if not dados.texto.strip():
        raise HTTPException(status_code=400, detail="O texto não pode estar vazio.")

    try:
        # Invoca o modelo através da interface LangChain
        resposta = llm.invoke(dados.texto)

        return {
            "texto_original": dados.texto,
            "texto_traduzido": resposta.strip(),
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao processar a tradução: {str(e)}"
        )
        