from app.embeddings.embedder import CodeEmbedder
from app.vectorstore.chroma_store import ChromaStore


class SemanticSearch:

    def __init__(self):
        self.embedder = CodeEmbedder()
        self.store = ChromaStore()

    def search(self, query, k=5):

        embedding = self.embedder.embed(query)

        results = self.store.search(embedding, k)

        return results


if __name__ == "__main__":

    search = SemanticSearch()

    while True:

        query = input("\nAsk about your repository (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        results = search.search(query)

        print("\nTop Matches\n")

        for i, doc in enumerate(results["documents"][0], 1):

            print("=" * 80)
            print(f"Result {i}")
            print("=" * 80)

            print(doc[:600])
            print()