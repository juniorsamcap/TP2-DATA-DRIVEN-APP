# Parte 2 - Questão 3: API de Tradução (Inglês -> Alemão) com LangChain e HuggingFace

Aplicação de tradução open-source desenvolvida com **FastAPI** e **LangChain**, integrada ao modelo de linguagem de código aberto **Helsinki-NLP/opus-mt-en-de** hospedado no Hugging Face.

---

## 1. Visão Geral e Benefícios da Arquitetura Open-Source

* **Gratuidade e Conformidade:** Execução 100% gratuita baseada em modelos open-source executados localmente, sem a necessidade de chaves de API pagas ou cadastro de cartão de crédito.
* **Privacidade de Dados:** O processamento é realizado totalmente em ambiente local via `transformers`, garantindo que os dados não sejam compartilhados com serviços de nuvem terceiros.
* **Orquestração Declarativa:** O LangChain padroniza a interface da LLM através de uma classe customizada (`LLM`), permitindo fácil substituição ou encadeamento com outras ferramentas da arquitetura.

---

## 2. Diagrama de Arquitetura e Fluxo de Dados

```mermaid
sequenceDiagram
    autonumber
    actor Cliente as Cliente (Swagger UI / Client)
    participant FastAPI as FastAPI (/traduzir)
    participant Pydantic as Schema Pydantic
    participant LangChain as LangChain (TradutorHuggingFaceLLM)
    participant HuggingFace as Modelo HuggingFace (opus-mt-en-de)

    Cliente->>FastAPI: POST /traduzir (JSON: {"texto": "..."})
    FastAPI->>Pydantic: Valida contrato de entrada (JSON -> Pydantic)
    Pydantic-->>FastAPI: Dados validados
    FastAPI->>LangChain: llm.invoke(texto)
    LangChain->>HuggingFace: Executa geração via AutoModelForSeq2SeqLM (Inglês -> Alemão)
    HuggingFace-->>LangChain: Retorna tokens traduzidos e decodificados
    LangChain-->>FastAPI: Retorna a string em alemão
    FastAPI-->>Cliente: HTTP 200 OK (JSON: {"texto_original": "...", "texto_traduzido": "..."})