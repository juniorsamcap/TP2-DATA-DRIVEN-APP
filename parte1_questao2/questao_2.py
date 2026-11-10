from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = FastAPI()

model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


class EntradaTraducao(BaseModel):
    texto: str


@app.post("/traduzir")
def traduzir_texto(dados: EntradaTraducao):
    inputs = tokenizer(dados.texto, return_tensors="pt")
    outputs = model.generate(**inputs)
    texto_traduzido = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"texto_original": dados.texto, "texto_traduzido": texto_traduzido}