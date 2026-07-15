from app.services.semantic_search import SemanticSearch
from app.llm.gemini_client import ask_gemini


class CodeDNAAgent:
    """
    CodeDNA AI Agent

    Uses:
    - Semantic Search
    - Gemini LLM
    - Repository Context
    """

    def __init__(self):
        self.search_engine = SemanticSearch()

    def ask(self, question: str):

        # Retrieve relevant repository code
        search_results = self.search_engine.search(question)

        # Prepare context
        context = "\n\n".join(
            str(result)
            for result in search_results
        )

        prompt = f"""
You are CodeDNA AI, a software architecture memory assistant.

Answer the user question using repository context.

Question:
{question}

Repository Context:
{context}

Explain:
1. Architecture
2. Important files
3. Data flow
4. Possible improvements
"""

        # Call Gemini
        answer = ask_gemini(prompt)

        return {
            "question": question,
            "answer": answer,
            "context": context
        }