import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load .env
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-flash-latest")

client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt: str):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"