from pathlib import Path

from analyzers.base_analyzer import BaseAnalyzer
from prompts.kubernetes_prompt import KUBERNETES_ANALYSIS_PROMPT


class KubernetesAnalyzer(BaseAnalyzer):

    def __init__(self):
        super().__init__()

    def analyze(self, kubernetes_path):

        manifests = ""

        for file in Path(kubernetes_path).glob("*.yaml"):
            manifests += f"\n\n# File: {file.name}\n"
            manifests += file.read_text()

        prompt = f"""
{KUBERNETES_ANALYSIS_PROMPT}

Kubernetes Manifests

{manifests}
"""

        return self.ask_ai(prompt)
