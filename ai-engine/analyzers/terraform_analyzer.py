from pathlib import Path

from analyzers.base_analyzer import BaseAnalyzer
from prompts.terraform_prompt import TERRAFORM_ANALYSIS_PROMPT


class TerraformAnalyzer(BaseAnalyzer):

    def __init__(self):
        super().__init__()

    def analyze(self, terraform_path):

        tf_files = ""

        for file in Path(terraform_path).rglob("*.tf"):

            tf_files += f"\n\n# File: {file.name}\n"

            tf_files += file.read_text()

        prompt = f"""
{TERRAFORM_ANALYSIS_PROMPT}

Terraform Configuration

{tf_files}
"""

        return self.ask_ai(prompt)
