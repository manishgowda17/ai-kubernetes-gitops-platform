import json

from services.gemini_service import GeminiService
from utils.platform_loader import PlatformLoader
from utils.json_parser import JSONParser

from prompts.platform_prompt import PLATFORM_SUMMARY_PROMPT


class RepositoryAnalyzer:

    def __init__(self, repo_path):

        self.loader = PlatformLoader(repo_path)
        self.ai = GeminiService()

    def analyze(self):

        infrastructure = self.loader.load()

        prompt = f"""
{PLATFORM_SUMMARY_PROMPT}

Analyze the following Platform Engineering repository.

Repository:

{json.dumps(infrastructure, indent=2)}
"""

        response = self.ai.generate_response(prompt)

        return JSONParser.parse(response)
