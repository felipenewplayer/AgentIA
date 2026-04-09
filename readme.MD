# 🤖 Agent com RAG (LangChain + Ollama)

Este projeto implementa um **Agent de IA com RAG (Retrieval-Augmented Generation)** utilizando LangChain e modelos locais via Ollama.

O sistema é capaz de **responder perguntas com base em documentos**, utilizando busca semântica em um banco vetorial e um modelo de linguagem como "cérebro".

---

## 🧠 Arquitetura

O projeto segue uma arquitetura modular baseada em separação de responsabilidades:

* **core** → modelo de linguagem (LLM) e memória
* **rag** → pipeline de recuperação (load, chunk, embeddings, banco vetorial)
* **tools** → ferramentas do agent (RAG como tool)
* **agent** → lógica de decisão
* **main** → ponto de entrada

---

## 📁 Estrutura do Projeto

```
app/
│
├── core/
│   ├── llm.py            # LLM (cérebro)
│   ├── memory.py         # memória (opcional)
│
├── rag/
│   ├── loader.py         # carregar documentos
│   ├── splitter.py       # chunking
│   ├── embeddings.py     # embeddings
│   ├── vector_store.py   # banco vetorial (Chroma)
│   ├── retriever.py      # busca semântica
│
├── tools/
│   ├── rag_tool.py       # RAG como tool
│
├── agent/
│   ├── agent.py          # lógica do agent
│
├── main.py               # execução
```

---

## ⚙️ Como executar o projeto

### 1. Criar ambiente virtual

```
python -m venv venv
venv\Scripts\activate
```

---

### 2. Instalar dependências

```
pip install langchain langchain-ollama langchain-chroma langchain-community langchain-text-splitters
```

---

### 3. Preparar os dados

Crie as pastas:

```
docs/
db/
```

Adicione seus arquivos dentro de `docs/`:

```
docs/
 └── text.txt
```

---

### 4. Rodar a aplicação

```
python app/main.py
```

---

## 🔄 Fluxo do Sistema

```
Usuário
   ↓
Agent (decide)
   ↓
Tool (RAG) → opcional
   ↓
LLM (gera resposta)
```

---

## 🧠 Conceitos

### 🔹 RAG (Retrieval-Augmented Generation)

Responsável por buscar informações relevantes nos documentos e fornecer contexto para o modelo.

### 🔹 Tool

Permite que o agent utilize funcionalidades externas, como o RAG.

### 🔹 Agent

Decide quando utilizar ferramentas ou responder diretamente.

### 🔹 LLM

Modelo de linguagem responsável por gerar a resposta final.

---

## 🚀 Tecnologias utilizadas

* Python
* LangChain (versão atualizada)
* Ollama (modelos locais como phi3)
* ChromaDB (banco vetorial)

---

## 💡 Possíveis melhorias

* Adicionar memória conversacional
* Criar múltiplas tools (API, cálculo, banco de dados)
* Melhorar a decisão do agent com LLM (ReAct)
* Criar API com FastAPI
* Interface web (React)

---

## 💥 Resumo

* RAG → busca informação
* Tool → expõe o RAG
* Agent → decide usar ou não
* LLM → gera resposta

---

## 📌 Objetivo

Este projeto foi desenvolvido com foco em aprendizado e construção de um **agent de IA do zero**, aplicando conceitos modernos como RAG, tools e LLMs locais.

---
