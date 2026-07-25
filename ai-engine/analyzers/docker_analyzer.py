from pathlib import Path

from services.gemini_service import GeminiService
from prompts.docker_prompt import DOCKER_ANALYSIS_PROMPT
from utils.json_parser import JSONParser


class DockerAnalyzer:

    def __init__(self):
        self.ai = GeminiService()

    def analyze(self, dockerfile_path):

        dockerfile = Path(dockerfile_path).read_text()

        prompt = f"""
{DOCKER_ANALYSIS_PROMPT}

Dockerfile:

{dockerfile}
"""

        response = self.ai.generate_response(prompt)
        return JSONParser.parse(response)
