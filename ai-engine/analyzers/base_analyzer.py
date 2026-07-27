from services.gemini_service import GeminiService
from utils.json_parser import JSONParser


class BaseAnalyzer:

    def __init__(self):
        self.ai = GeminiService()

    def ask_ai(self, prompt):

        response = self.ai.generate_response(prompt)

        return JSONParser.parse(response)
