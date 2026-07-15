import chromadb


class ChromaStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./database")

        self.collection = self.client.get_or_create_collection(
            name="codedna"
        )

    def add_document(self, doc_id, text, embedding):

        # Delete existing document if it already exists
        try:
            self.collection.delete(ids=[doc_id])
        except Exception:
            pass

        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embedding]
        )

    def search(self, embedding, k=5):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )


if __name__ == "__main__":

    store = ChromaStore()

    print("ChromaDB initialized successfully.")