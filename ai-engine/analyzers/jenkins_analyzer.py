from pathlib import Path

from analyzers.base_analyzer import BaseAnalyzer
from prompts.jenkins_prompt import JENKINS_ANALYSIS_PROMPT


class JenkinsAnalyzer(BaseAnalyzer):

    def __init__(self):
        super().__init__()

    def analyze(self, jenkinsfile_path):

        jenkinsfile = Path(jenkinsfile_path).read_text()

        prompt = f"""
{JENKINS_ANALYSIS_PROMPT}

Jenkinsfile

{jenkinsfile}
"""

        return self.ask_ai(prompt)
