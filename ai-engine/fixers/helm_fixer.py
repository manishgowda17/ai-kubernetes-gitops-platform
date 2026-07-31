from pathlib import Path

from services.gemini_service import GeminiService
from prompts.helm_fix_prompt import HELM_FIX_PROMPT


class HelmFixer:

    def __init__(self):
        self.ai = GeminiService()

    def fix(self, helm_folder):

        chart = ""

        for file in Path(helm_folder).rglob("*"):

            if file.is_file():
                chart += file.read_text() + "\n\n"

        prompt = f"""
{HELM_FIX_PROMPT}

{chart}
"""

        return self.ai.generate_response(prompt)
