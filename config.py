"""Loads .env file and exposes LLM configuration."""
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY", "")
BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
