# Parte 1 - Questão 1: Geração de Texto com FastAPI e Hugging Face (GPT-2)

Aplicação desenvolvida em FastAPI que utiliza o modelo GPT-2 da biblioteca Transformers (Hugging Face) para gerar continuações de texto a partir de uma entrada enviada via requisição HTTP POST.

## Pré-requisitos e Instalação

1. Certifique-se de ter o Python instalado e o ambiente virtual ativado no VS Code.
2. Instale as bibliotecas necessárias executando o comando no terminal:
   ```powershell
   pip install fastapi uvicorn transformers torch pydantic