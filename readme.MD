#  AI Agent com LangChain + Ollama (RAG + Tools)

Este projeto implementa um **AI Agent** utilizando **LangChain** e modelos locais via **Ollama**, com suporte a **RAG (Retrieval-Augmented Generation)** e uso de **tools** para ampliar as capacidades do agente.

O sistema é capaz de **responder perguntas com base em contexto externo**, utilizando busca semântica em um banco vetorial combinado com um modelo de linguagem (LLM) como “cérebro”.

---

## Arquitetura

O projeto segue uma arquitetura modular baseada em separação de responsabilidades:

* **core** → modelo de linguagem (LLM) e memória
* **rag** → pipeline de recuperação (load, chunk, embeddings, banco vetorial)
* **tools** → ferramentas utilizadas pelo agent
* **agent** → lógica de decisão (quando usar tools ou responder diretamente)
* **main** → ponto de entrada da aplicação

---

##  Estrutura do Projeto

```
app/
│
├── core/
│   ├── llm.py            # LLM (cérebro)
│   ├── memory.py         # memória (opcional)
│
├── rag/
│   ├── loader.py         # carregamento de documentos
│   ├── splitter.py       # chunking de texto
│   ├── embeddings.py     # geração de embeddings
│   ├── vector_store.py   # banco vetorial (Chroma)
│   ├── retriever.py      # busca semântica
│
├── tools/                # definição de tools do agent
│
├── agent/
│   ├── agent.py          # lógica do agent
│
├── main.py               # execução da aplicação
```

---

##  Como executar o projeto

### 1. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 2. Instalar dependências

Crie um arquivo `requirements.txt` com as dependências do projeto ou instale manualmente:

```bash
pip install langchain langchain-ollama langchain-chroma langchain-community langchain-text-splitters
```

---

### 3. Instalar e executar o Ollama

Baixe o Ollama:

https://ollama.com/download

Após instalar, execute um modelo local:

```bash
ollama run phi3
```

> Você pode utilizar outros modelos compatíveis com o Ollama.

---

### 4. Preparar os dados

Crie as pastas:

```bash
docs/
db/
```

Adicione arquivos dentro de `docs/`:

```
docs/
 └── text.txt
```

---

### 5. Rodar a aplicação

```bash
python app/main.py
```

---

##  Fluxo do Sistema

```
Usuário
   ↓
Agent (decide se utiliza tools ou responde diretamente)
   ↓
Tool (RAG) → opcional
   ↓
LLM (gera resposta)
```

---

## Conceitos

###  RAG (Retrieval-Augmented Generation)

Responsável por buscar informações relevantes nos documentos e fornecer contexto adicional para o modelo gerar respostas mais precisas.

---

###  Tool

Permite que o agent utilize funcionalidades externas, como busca em documentos, APIs ou cálculos.

---

###  Agent

Responsável por decidir quando utilizar ferramentas ou responder diretamente com base no contexto.

---

###  LLM (Large Language Model)

Modelo de linguagem responsável por interpretar a pergunta e gerar a resposta final.

---

##  Tecnologias utilizadas

* Python
* LangChain
* Ollama (modelos locais como phi3)
* ChromaDB (banco vetorial)

---

##  Exemplo de uso

**Pergunta:**

> "Qual é o conteúdo do documento?"

**Resposta:**

O agent utiliza RAG para buscar informações relevantes no banco vetorial e gerar uma resposta baseada no contexto encontrado nos documentos.

---

## Possíveis melhorias

* Adicionar memória conversacional persistente
* Criar múltiplas tools (API externa, cálculos, banco de dados)
* Implementar estratégia ReAct para tomada de decisão
* Expor o agent via API (FastAPI)
* Criar interface web (React)

---

##  Objetivo

Este projeto foi desenvolvido com foco em aprendizado e construção de um **AI Agent do zero**, aplicando conceitos modernos como RAG, tools e LLMs locais.

---

##  Observações

* Projeto voltado para estudo e experimentação
* Pode ser expandido para aplicações reais com APIs e interfaces

---
