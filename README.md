<div align="center">

# 🩺 MedAssist AI — Medical Chatbot

**An AI-powered medical assistant built on Hutchinson's Clinical Methods**

Retrieval-Augmented Generation (RAG) chatbot that answers evidence-based medical questions using vector-searched context from Hutchinson's clinical method textbook.

[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1+-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![LangChain](https://img.shields.io/badge/LangChain-1.2+-1C3C3C?logo=langchain&logoColor=white)](https://langchain.com)
[![Pinecone](https://img.shields.io/badge/Pinecone-Vector_DB-00C5CD)](https://pinecone.io)

---

![MedAssist AI Dark UI](https://img.shields.io/badge/UI-Dark_Theme-1F2937?style=for-the-badge)

</div>

## ✨ Features

- 🤖 **RAG-powered answers** — retrieves the most relevant chunks from medical textbooks before generating a response
- 📚 **Hutchinson's Clinical Methods** — built on one of the most trusted clinical reference texts
- 🧠 **Groq LLM inference** — fast responses via the Groq API
- 🌲 **Pinecone vector store** — semantic search across chunked medical documents
- 🎨 **Beautiful dark-themed UI** — modern, responsive chat interface with markdown & table rendering
- ⚡ **Real-time chat** — typing indicators, animated transitions, and quick-prompt suggestions

## 🏗️ Architecture

```
User Question
    │
    ▼
┌──────────┐     ┌───────────────┐     ┌──────────────┐
│  Flask    │────▶│  LangChain    │────▶│   Pinecone   │
│  Frontend │     │  RAG Chain    │     │  Vector DB   │
└──────────┘     └───────┬───────┘     └──────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │   Groq LLM   │
                  │  (GPT-oss)   │
                  └──────────────┘
                         │
                         ▼
                   AI Response
```

## 📁 Project Structure

```
medical_chatbot/
├── app.py                 # Flask application & routes
├── store_index.py         # Script to ingest PDFs into Pinecone
├── src/
│   ├── __init__.py
│   ├── helper.py          # PDF loading, text splitting, embeddings
│   └── prompt.py          # System prompt template
├── templates/
│   └── chat.html          # Chat UI (HTML + JavaScript)
├── static/
│   └── style.css          # Dark-themed stylesheet
├── data/                  # Place your PDF textbooks here
├── requirements.txt
├── pyproject.toml
├── setup.py
└── .env                   # API keys (not committed)
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.14+**
- A [**Pinecone**](https://pinecone.io) account (free tier works)
- A [**Groq**](https://console.groq.com) API key

### 1. Clone the Repository

```bash
git clone https://github.com/Theoph-ay/medical_chatbot.git
cd medical_chatbot
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=your_index_name_here
GROQ_API_KEY=your_groq_api_key_here
```

> **Note:** You need to create a Pinecone index first via the [Pinecone console](https://app.pinecone.io). Use **384 dimensions** (matching the `all-MiniLM-L6-v2` embedding model) with **cosine** metric.

### 5. Ingest Your Medical PDFs

Place your PDF files (e.g., Hutchinson's Clinical Methods) into the `data/` folder, then run:

```bash
python store_index.py
```

This will:
- Load all PDFs from the `data/` directory
- Split them into 500-character chunks with 20-character overlap
- Generate embeddings using `sentence-transformers/all-MiniLM-L6-v2`
- Upload the vectors to your Pinecone index

### 6. Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core language |
| **Flask** | Web framework & API server |
| **LangChain** | RAG orchestration (retrieval chain + stuff documents chain) |
| **Pinecone** | Vector database for semantic search |
| **Groq** | LLM inference (fast cloud-based generation) |
| **Sentence Transformers** | Embedding model (`all-MiniLM-L6-v2`) |
| **PyPDF** | PDF document loading |
| **HTML/CSS/JS** | Frontend chat interface |

## 📝 How It Works

1. **PDF Ingestion** — `store_index.py` reads medical PDFs, splits them into chunks, embeds them, and stores vectors in Pinecone.
2. **User Query** — The user types a medical question in the chat UI.
3. **Retrieval** — LangChain's retriever fetches the top 6 most relevant chunks from Pinecone.
4. **Generation** — The retrieved context + question are passed to the Groq LLM, which generates a clinical, evidence-based answer.
5. **Display** — The response is rendered in the chat with markdown formatting, including tables, lists, and code blocks.

## ⚠️ Disclaimer

> MedAssist AI is designed for **educational and informational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical decisions.

## 📄 License

This project is open source.

---

<div align="center">

**Built with ❤️ using Python, Flask, LangChain & Pinecone**

</div>
