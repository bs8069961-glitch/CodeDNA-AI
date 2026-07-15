from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME")

    CHROMA_DB = os.getenv("CHROMA_DB")

    REPOSITORY_PATH = os.getenv("REPOSITORY_PATH")

    NEO4J_URI = os.getenv("NEO4J_URI")

    NEO4J_USER = os.getenv("NEO4J_USER")

    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


settings = Settings()