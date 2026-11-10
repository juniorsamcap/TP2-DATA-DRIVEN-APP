from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# 1. Criação da aplicação FastAPI
app = FastAPI()

# 2. Carregamento do pipeline de geração de texto com o modelo GPT-2
generator = pipeline("text-generation", model="gpt2")


# 3. Definição da estrutura dos dados de entrada
class EntradaTexto(BaseModel):
    texto: str


# 4. Rota POST que recebe a frase e gera a continuação
@app.post("/gerar-texto")
def gerar_texto(dados: EntradaTexto):
    # Gera a continuação a partir do texto enviado (limitado a 50 caracteres para ser rápido)
    resultado = generator(
        dados.texto, max_length=50, num_return_sequences=1, pad_token_id=50256
    )

    # Extrai o texto gerado da resposta do modelo
    texto_gerado = resultado[0]["generated_text"]

    # Retorna como resposta em formato JSON
    return {"texto_gerado": texto_gerado}





