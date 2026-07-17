from sentence_transformers import SentenceTransformer
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CodeEmbedder:
    """
    Generates vector embeddings for code and text using
    the all-MiniLM-L6-v2 SentenceTransformer model.
    """

    _model = None

    def __init__(self):
        if CodeEmbedder._model is None:
            logger.info("Loading embedding model (all-MiniLM-L6-v2)...")
            CodeEmbedder._model = SentenceTransformer("all-MiniLM-L6-v2")
            logger.info("Embedding model loaded successfully.")

        self.model = CodeEmbedder._model

    def embed(self, text: str) -> List[float]:
        """
        Generate an embedding for a single string.
        """
        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple strings.
        """
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embeddings.tolist()
        
