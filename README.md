
# DevConnect AI

AI-powered assistant for understanding and navigating the **DevConnect codebase** using **Retrieval-Augmented Generation (RAG)**.

This project indexes repositories, generates embeddings for code and documentation, stores them in a vector database, and allows developers to query the codebase using natural language.

The system retrieves relevant code snippets and uses an LLM to generate contextual answers with source references.

---

# Features

- Repository ingestion and indexing
- Language-aware code chunking (Java, Markdown, YAML, etc.)
- Embedding generation with SentenceTransformers
- Vector search using Qdrant
- Retrieval-Augmented Generation (RAG)
- LLM support (OpenAI or Ollama)
- Token usage monitoring
- Source attribution in responses
- REST API for querying the system
- Debug endpoint for vector search inspection

---

# Architecture

The system follows a modular architecture separating ingestion, retrieval, and generation layers.

```
User Query
    ↓
Embedding Service
    ↓
Vector Search (Qdrant)
    ↓
Context Builder
    ↓
LLM Client (OpenAI / Ollama)
    ↓
Generated Answer
```

Project structure:

```
src/
 ├─ api/                # FastAPI endpoints
 │
 ├─ ingestion/          # Repository ingestion pipeline
 │   ├─ chunk/          # Code chunkers per language
 │   └─ sync/           # Repository synchronization
 │
 ├─ embeddings/         # Embedding generation
 │
 ├─ vectorstore/        # Vector database abstraction
 │   └─ qdrant_store.py
 │
 ├─ retrieval/          # Query orchestration
 │   ├─ query_service.py
 │   └─ context_builder.py
 │
 ├─ llm/                # LLM clients
 │   ├─ client.py
 │   ├─ openai_client.py
 │   ├─ ollama_client.py
 │   └─ factory.py
```

---

# Requirements

- Python 3.10+
- Docker (for Qdrant)
- Ollama (optional for local LLM)

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/devconnect-ai.git
cd devconnect-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running Qdrant

The project uses **Qdrant** as the vector database.

Start Qdrant with Docker:

```bash
docker compose up -d
```

Qdrant dashboard:

```
http://localhost:6333/dashboard
```

---

# Environment Configuration

Create a `.env` file:

```
LLM_PROVIDER=ollama

OLLAMA_MODEL=gemma3:4b
OLLAMA_URL=http://localhost:11434

OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4o-mini
```

You can easily switch providers by changing:

```
LLM_PROVIDER=openai
```

---

# Running Ollama (optional)

Install Ollama:

https://ollama.com

Pull a model:

```bash
ollama pull gemma3:4b
```

Run the model:

```bash
ollama run gemma3:4b
```

---

# Indexing Repositories

Run the ingestion pipeline:

```bash
python scripts/sync_and_ingest.py
```

This will:

1. Sync repositories
2. Chunk source code
3. Generate embeddings
4. Store vectors in Qdrant

---

# Running the API

Start the API server:

```bash
uvicorn api.app:app --reload
```

API documentation:

```
http://localhost:8000/docs
```

---

# Query Endpoint

Ask questions about the indexed codebase.

```
POST /query
```

Request:

```json
{
  "question": "How does password recovery work?"
}
```

Response:

```json
{
  "answer": "...",
  "sources": [
    "CompletePasswordRecoveryUseCaseImpl.java"
  ],
  "usage": {
    "prompt_tokens": 780,
    "completion_tokens": 210,
    "total_tokens": 990
  }
}
```

---

# Search Endpoint

Debug retrieval without LLM generation.

```
GET /search?q=password recovery
```

Response:

```json
{
  "query": "password recovery",
  "results": [
    {
      "score": 0.87,
      "file": "CompletePasswordRecoveryUseCaseImpl.java",
      "chunk": "public class CompletePasswordRecoveryUseCaseImpl..."
    }
  ]
}
```

---

# Supported LLM Providers

The system supports multiple LLM backends through a provider abstraction.

Currently supported:

- OpenAI
- Ollama

The provider can be selected via environment variable.

---

# Token Usage Monitoring

The API returns token usage information to help track costs and optimize prompts.

```
prompt_tokens
completion_tokens
total_tokens
```

This allows tuning the context size and improving performance.

---

# Roadmap

Planned improvements:

- Hybrid search (vector + keyword)
- Re-ranking for improved retrieval
- Context compression
- Multi-language query handling
- Slack integration
- VSCode extension
- Web UI
- Repository map generation

---

# Use Cases

- Codebase exploration
- Developer onboarding
- Architecture discovery
- Code search
- Documentation assistant

---

# License

MIT License
