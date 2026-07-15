from sentence_transformers import SentenceTransformer


class CodeEmbedder:
    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, text: str):
        return self.model.encode(text).tolist()


if __name__ == "__main__":
    embedder = CodeEmbedder()

    text = """
    def hello():
        print("Hello World")
    """

    vector = embedder.embed(text)

    print(f"Embedding size: {len(vector)}")
    print(vector[:10])