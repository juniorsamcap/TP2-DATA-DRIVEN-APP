# Parte 2 - Questão 1: Chatbot Protótipo com Fake LLM e LangChain

Protótipo de chatbot desenvolvido com **FastAPI** e **LangChain**, utilizando a classe `FakeListLLM` para simular inferências de modelos de linguagem sem a necessidade de chaves de API externas ou alto processamento computacional.

---

## 1. Importância do Uso de Fake LLM para Testes Rápido

* **Custo Zero e Sem Dependência de Chaves de API:** Permite o desenvolvimento e a validação de fluxos de trabalho sem consumir créditos de provedores pagos ou depender de tokens de acesso durante o ciclo de desenvolvimento.
* **Velocidade de Execução (Latência Praticamente Nula):** Como as respostas são pré-definidas em memória, o ciclo de requisição/resposta é executado em milissegundos, agilizando testes unitários e de integração.
* **Determinismo e Testabilidade:** Garantia de respostas previsíveis para validação do esquema de dados (`Pydantic`), tratamento de erros e integração da API no FastAPI sem variações aleatórias típicas de modelos de linguagem reais.
* **Isolamento de Componentes:** Permite validar a arquitetura da aplicação e os *end-points* HTTP de forma independente do provedor de inteligência artificial.

---

## 2. Diagrama de Arquitetura e Fluxo de Dados

```mermaid
sequenceDiagram
    autonumber
    actor Cliente as Cliente (Swagger UI / Client)
    participant FastAPI as FastAPI (/chat)
    participant Model as Pydantic (EntradaMensagem)
    participant LangChain as LangChain (FakeListLLM)

    Cliente->>FastAPI: POST /chat (JSON: {"mensagem": "..."})
    FastAPI->>Model: Valida contrato de entrada (JSON -> Pydantic)
    Model-->>FastAPI: Dados validados
    FastAPI->>LangChain: llm.invoke(mensagem)
    LangChain-->>FastAPI: Retorna próxima resposta simulada da lista
    FastAPI-->>Cliente: HTTP 200 OK (JSON: {"mensagem_usuario": "...", "resposta_chatbot": "..."})