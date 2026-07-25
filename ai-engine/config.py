from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")

# Gemini Model
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
