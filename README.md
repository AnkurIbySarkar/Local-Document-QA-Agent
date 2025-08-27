# 🦙 Local QA Agent for Documents

Chat with your own documents — thesis papers, PDFs, research articles, notes, even images — fully local on your laptop.

- **LangChain** → document loading, chunking, retrieval  
- **Ollama + Llama 3.2 Vision** → local LLM for text & image Q&A  
- **Gradio (optional)** → simple web UI  
- **uv** → fast, modern Python packaging & environment management  

Everything runs offline and your files stay private.

---

## Features

- Ask natural questions about long PDFs (e.g., “What methods are used in Chapter 3?”)
- Works with multiple files and large docs
- Optional image understanding via Vision model
- Clean, reproducible setup with uv

---

## 🛠️ Prerequisites

### 1. Install Ollama

- **macOS:**
brew install ollama

text
- **Linux:** Follow instructions at https://ollama.com/download
- **Windows:** Official installer at https://ollama.com/download

#### Pull models
ollama pull llama3.2-vision # main QA model (text+images)
ollama pull nomic-embed-text # recommended embedding model

or: ollama pull mxbai-embed-large
text

---

### 2. Install uv

- **Linux/macOS:**
curl -LsSf https://astral.sh/uv/install.sh | sh

text
- **Windows (PowerShell):**
irm https://astral.sh/uv/install.ps1 | iex

text

---

## pyproject.toml (for uv)

Add this file at the project root:

[project]
name = "local-qa-agent"
version = "0.1.0"
description = "Chat with local documents using LangChain + Ollama (Llama 3.2 Vision)"
readme = "README.md"
requires-python = ">=3.10"

dependencies = [
"langchain>=0.3",
"langchain-community>=0.3",
"langchain-ollama>=0.2",
"pypdf>=4.0",
"gradio>=4.0",

Choose ONE vector store (FAISS preferred; Chromadb as fallback, esp. on Windows):
"faiss-cpu>=1.8; platform_system != 'Windows'",
"chromadb>=0.5",
]

[tool.uv]

Optional: speed up resolution, lockfile settings, etc.
[tool.uv.sources]

(optional) custom sources or mirrors
text

> **Why both FAISS & Chroma?**  
> FAISS is fast and popular; on Windows it can be tricky to build, so Chroma is included as a portable fallback.

---

## Installation (with uv)

1) Clone your repo
git clone https://github.com/AnkurIbySarkar/Local-Document-QA-Agent/tree/master
cd local-qa-agent

2) Create the environment and install deps
uv sync

3) (Optional) Activate venv if you prefer
uv manages execution without activation, but you can:
macOS/Linux
source .venv/bin/activate

Windows
.venv\Scripts\activate

text

---

## ▶Usage

1. **Start Ollama (if it’s not already running)**
uv run main.py


Then open the printed local URL, upload/select your PDF(s), and ask questions like:
- “Summarize the methodology section.”
- “List the key findings from the results chapter.”
- “What limitations are noted in the conclusion?”

---

## Notes & Tips

- **Embeddings:** using `nomic-embed-text` or `mxbai-embed-large` via Ollama works well for retrieval.
- **Chunking:** start with 1,000–1,500 token chunks and ~150–250 overlap; tune per document style.
- **Vector store:** FAISS is fast; if install issues arise (often on Windows), use Chroma.
- **Images:** Vision model can answer questions about figures/diagrams if you feed image inputs in your UI/app.

---

## Troubleshooting

- “Model not found” → run `ollama pull llama3.2-vision` and your chosen embedding model.
- FAISS install issues on Windows → rely on Chroma (already in deps).
- Ollama connection errors → ensure `ollama serve` is running; default is [http://127.0.0.1:11434](http://127.0.0.1:11434).
- Slow answers → reduce top_k docs, lower chunk size, or try a lighter model via Ollama.

---


