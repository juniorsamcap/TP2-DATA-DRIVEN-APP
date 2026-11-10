# Parte 2 - Questão 2: API de Tradução com LangChain e OpenAI (Simulado)

API de tradução de texto de Inglês para Francês desenvolvida com **FastAPI** e **LangChain**, projetada para integrar com modelos da OpenAI (com fallback simulado via `FakeListLLM` para testes sem custo e validação contínua).

---

## 1. Visão Geral e Benefícios da Arquitetura

* **Baixa Latência e Testabilidade:** A integração desacoplada via LangChain permite chavear entre provedores de nuvem e mocks de testes sem alterar as rotas HTTP da aplicação.
* **Orquestração via LangChain:** Estrutura o fluxo de tradução e o gerenciamento de dados de forma declarativa.
* **Validação de Dados com Pydantic:** Garante o contrato da API (`EntradaTraducao`), validando requisições e estruturando a resposta JSON de retorno.

---

## 2. Diagrama de Arquitetura e Fluxo de Dados

```mermaid
sequenceDiagram
    autonumber
    actor Cliente as Cliente (Swagger UI / Client)
    participant FastAPI as FastAPI (/traduzir)
    participant Pydantic as Schema Pydantic
    participant LangChain as LangChain (LLM / Chain)
    participant Model as Provedor LLM (OpenAI / FakeLLM)

    Cliente->>FastAPI: POST /traduzir (JSON: {"texto": "..."})
    FastAPI->>Pydantic: Valida contrato de entrada (JSON -> Pydantic)
    Pydantic-->>FastAPI: Dados validados
    FastAPI->>LangChain: llm.invoke(texto)
    LangChain->>Model: Processa o prompt de tradução (Inglês -> Francês)
    Model-->>LangChain: Retorna o texto traduzido
    LangChain-->>FastAPI: Conteúdo traduzido
    FastAPI-->>Cliente: HTTP 200 OK (JSON: {"texto_original": "...", "texto_traduzido": "..."})