import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")

# Gemini Model
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

# Repository Path
REPOSITORY_PATH = os.getenv("REPOSITORY_PATH", "..")
