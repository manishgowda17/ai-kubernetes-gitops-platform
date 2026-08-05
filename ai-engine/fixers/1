from pathlib import Path

from services.gemini_service import GeminiService
from prompts.terraform_fix_prompt import TERRAFORM_FIX_PROMPT


class TerraformFixer:

    def __init__(self):
        self.ai = GeminiService()

    def fix(self, terraform_folder):

        tf = ""

        for file in Path(terraform_folder).glob("*.tf"):
            tf += file.read_text() + "\n\n"

        prompt = f"""
{TERRAFORM_FIX_PROMPT}

{tf}
"""

        return self.ai.generate_response(prompt)
