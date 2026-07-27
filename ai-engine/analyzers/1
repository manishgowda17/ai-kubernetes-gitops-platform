from pathlib import Path

from analyzers.base_analyzer import BaseAnalyzer
from prompts.docker_prompt import DOCKER_ANALYSIS_PROMPT


class DockerAnalyzer(BaseAnalyzer):

    def __init__(self):
        super().__init__()

    def analyze(self, dockerfile_path):

        dockerfile = Path(dockerfile_path).read_text()

        prompt = f"""
{DOCKER_ANALYSIS_PROMPT}

Dockerfile

{dockerfile}
"""

        return self.ask_ai(prompt)
