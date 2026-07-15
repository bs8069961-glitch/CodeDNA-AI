from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

app = FastAPI(
    title="CodeDNA AI",
    version="1.0.0",
    description="AI-powered Software Architecture Memory Agent",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API routes
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to CodeDNA AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "message": "Backend is running successfully."
    }


@app.get("/about")
def about():
    return {
        "project": "CodeDNA AI",
        "version": "1.0.0",
        "description": "AI-powered Software Architecture Memory Agent",
        "features": [
            "Repository Scanner",
            "AST Parser",
            "Dependency Graph",
            "Architecture Analyzer",
            "SentenceTransformer Embeddings",
            "ChromaDB Vector Store",
            "Semantic Search"
        ]
    }


@app.get("/status")
def status():
    return {
        "server": "running",
        "api": "online"
    }