from pathlib import Path

from analyzers.base_analyzer import BaseAnalyzer
from prompts.helm_prompt import HELM_ANALYSIS_PROMPT


class HelmAnalyzer(BaseAnalyzer):

    def __init__(self):
        super().__init__()

    def analyze(self, helm_path):

        chart = ""

        for file in Path(helm_path).rglob("*"):

            if file.is_file():

                chart += f"\n\n# File: {file.relative_to(helm_path)}\n"
                chart += file.read_text()

        prompt = f"""
{HELM_ANALYSIS_PROMPT}

Helm Chart

{chart}
"""

        return self.ask_ai(prompt)
