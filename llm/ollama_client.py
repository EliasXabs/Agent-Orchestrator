import requests
from config import OLLAMA_BASE_URL, OLLAMA_MODEL, LLM_TEMPERATURE


class OllamaClient:

    def generate(self, prompt: str) -> str:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": LLM_TEMPERATURE
                }
            }
        )

        response.raise_for_status()

        return response.json()["response"]