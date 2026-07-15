from pathlib import Path

from app.parser.repository_scanner import RepositoryScanner
from app.embeddings.embedder import CodeEmbedder
from app.vectorstore.chroma_store import ChromaStore


class RepositoryIndexer:

    def __init__(self, repo_path="."):
        self.repo_path = repo_path
        self.embedder = CodeEmbedder()
        self.store = ChromaStore()

    def index(self):

        scanner = RepositoryScanner(self.repo_path)
        files = scanner.get_python_files()

        print(f"\nFound {len(files)} Python files.\n")

        indexed = 0

        for file in files:

            try:
                with open(file, "r", encoding="utf-8") as f:
                    code = f.read()

                embedding = self.embedder.embed(code)

                self.store.add_document(
                    doc_id=str(file),
                    text=code,
                    embedding=embedding,
                )

                print(f"✅ Indexed: {file}")
                indexed += 1

            except Exception as e:
                print(f"❌ Skipped {file}: {e}")

        print("\n========================")
        print(f"Indexed {indexed} files.")
        print("========================")


if __name__ == "__main__":
    RepositoryIndexer(".").index()