from fastapi import APIRouter
from pydantic import BaseModel

from app.services.repository_indexer import RepositoryIndexer
from app.services.semantic_search import SemanticSearch
from app.analyzer.architecture_analyzer import ArchitectureAnalyzer
from app.services.ai_agent import CodeDNAAgent


router = APIRouter()


# -----------------------------
# Request Models
# -----------------------------

class SearchRequest(BaseModel):
    query: str


class AskRequest(BaseModel):
    question: str


# -----------------------------
# Basic Route
# -----------------------------

@router.get("/")
def root():
    return {
        "message": "Welcome to CodeDNA AI"
    }


# -----------------------------
# Repository Indexing
# -----------------------------

@router.post("/index")
def index_repository():

    indexer = RepositoryIndexer(".")
    indexer.index()

    return {
        "status": "success",
        "message": "Repository indexed successfully"
    }


# -----------------------------
# Semantic Search
# -----------------------------

@router.post("/search")
def search_repository(request: SearchRequest):

    search = SemanticSearch()

    results = search.search(
        request.query
    )

    return {
        "query": request.query,
        "results": results
    }


# -----------------------------
# Architecture Analysis
# -----------------------------

@router.get("/architecture")
def architecture():

    analyzer = ArchitectureAnalyzer(".")

    return analyzer.analyze()


# -----------------------------
# CodeDNA AI Agent
# -----------------------------

@router.post("/ask")
def ask_agent(request: AskRequest):

    agent = CodeDNAAgent()

    response = agent.ask(
        request.question
    )

    return response