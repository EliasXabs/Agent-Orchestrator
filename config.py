import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.2))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 5))
WORKSPACE_PATH = os.getenv("WORKSPACE_PATH", "workspace")