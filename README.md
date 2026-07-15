 CodeDNA AI
AI-Powered Software Architecture Memory Agent

> Understand any codebase using AI-powered semantic search, repository indexing, and architecture-aware analysis.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![SentenceTransformers](https://img.shields.io/badge/Embeddings-SentenceTransformers-red)
![License](https://img.shields.io/badge/License-MIT-blue)

 Overview

CodeDNA AI is an AI-powered software architecture assistant that enables developers to understand large codebases through natural language.

Instead of manually exploring hundreds of source files, developers can ask questions such as:

- Explain the architecture of this repository.
- Which files implement semantic search?
- How does repository indexing work?
- Show the dependency flow.
- Where is the embedding model used?

CodeDNA AI analyzes the repository, builds a semantic knowledge base using vector embeddings, and generates architecture-aware answers using Google Gemini.
 Features
 - Repository indexing
- AST-based Python code parsing
- Dependency graph generation
- Semantic code search
- ChromaDB vector storage
- Sentence Transformer embeddings
- Google Gemini integration
- FastAPI REST APIs
- Architecture analysis
- AI-powered repository question answering

Architecture

                    +--------------------+
                    |     Developer      |
                    +---------+----------+
                              |
                              |
                              ▼
                     FastAPI REST API
                              |
             +----------------+----------------+
             |                                 |
             ▼                                 ▼
    Repository Indexer               Architecture Analyzer
             |                                 |
             ▼                                 ▼
      Python Repository                 AST Parser
             |
             ▼
   Sentence Transformer
        Embeddings
             |
             ▼
        ChromaDB
      Vector Database
             |
             ▼
     Semantic Search
             |
             ▼
      Google Gemini
             |
             ▼
     AI Generated Answere 
     
     Project Structure

backend/

│── app/
│   ├── analyzer/
│   │      architecture_analyzer.py
│   │
│   ├── api/
│   │      routes.py
│   │
│   ├── embeddings/
│   │      embedder.py
│   │
│   ├── llm/
│   │      gemini_client.py
│   │
│   ├── parser/
│   │      repository_scanner.py
│   │      ast_parser.py
│   │      dependency_graph.py
│   │
│   ├── services/
│   │      repository_indexer.py
│   │      semantic_search.py
│   │      ai_agent.py
│   │
│   ├── vectorstore/
│   │      chroma_store.py
│   │
│   └── main.py
│
├── tests/
├── database/
├── requirements.txt
└── README.md
```

---

 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| FastAPI | REST APIs |
| Google Gemini | Large Language Model |
| Sentence Transformers | Code Embeddings |
| ChromaDB | Vector Database |
| AST | Static Code Analysis |
| Pydantic | Data Validation |

---
 Workflow

 Step 1

Repository Scanner discovers Python source files.

↓

### Step 2

AST Parser extracts:

- Functions
- Classes
- Imports

↓

### Step 3

Repository Indexer generates embeddings.

↓

### Step 4

Embeddings are stored inside ChromaDB.

↓

### Step 5

Semantic Search retrieves the most relevant code.

↓

### Step 6

Google Gemini receives repository context.

↓

### Step 7

CodeDNA AI produces architecture-aware answers.

---

 REST API

## Index Repository

```
POST /index
```

Indexes the repository into ChromaDB.

---

## Semantic Search

```
POST /search
```

Searches repository code using semantic similarity.

---

## Repository Architecture

```
GET /architecture
```

Returns architectural grouping of the repository.

---

## Ask AI

```
POST /ask
```

Example

```json
{
    "question":"Explain the architecture of this repository"
}
```

---

# Example Questions

- Explain the architecture.
- Which files handle embeddings?
- How is semantic search implemented?
- Explain repository indexing.
- Show dependency flow.
- Which modules interact with ChromaDB?
- How does FastAPI connect to Gemini?

---

#  Current Capabilities

✅ Repository indexing

✅ Semantic search

✅ AST parsing

✅ Dependency graph generation

✅ Architecture analysis

✅ AI-powered repository Q&A

✅ Vector search using ChromaDB

---

# 🚀 Future Improvements

- Multi-language support
- GitHub repository URL indexing
- Interactive dependency visualization
- Code quality analysis
- Security vulnerability detection
- Automatic documentation generation
- Docker deployment
- CI/CD with GitHub Actions
- Authentication & user management

# 👨‍💻 Author

**Bhanu Singh**

B.Tech Graduate | Software Developer | AI & Backend Enthusiast

GitHub:
https://github.com/bs8069961-glitch

 
 Why CodeDNA AI?

Understanding a new codebase often requires reading hundreds of files.

CodeDNA AI accelerates onboarding by combining semantic search, static code analysis, vector databases, and Large Language Models to help developers explore repositories using natural language.

It serves as an intelligent software architecture assistant for developers, interviewers, and engineering teams.

---

If you found this project useful, consider giving it a ⭐ on GitHub.
