from services.gemini_service import GeminiService
from prompts.helm_prompt import HELM_ANALYSIS_PROMPT
from utils.helm_loader import HelmLoader
from utils.json_parser import JSONParser


class HelmAnalyzer:

    def __init__(self):
        self.ai = GeminiService()

    def analyze(self, chart_directory):

        loader = HelmLoader(chart_directory)

        files = loader.load_chart()

        combined_chart = ""

        for file in files:

            combined_chart += f"""

File:
{file['filename']}

Content:

{file['content']}

------------------------------------

"""

        prompt = f"""
{HELM_ANALYSIS_PROMPT}

Helm Chart:

{combined_chart}
"""

        response = self.ai.generate_response(prompt)

        return JSONParser.parse(response)
