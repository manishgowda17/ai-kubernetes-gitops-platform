from services.gemini_service import GeminiService
from prompts.jenkins_prompt import JENKINS_ANALYSIS_PROMPT
from utils.jenkins_loader import JenkinsLoader
from utils.json_parser import JSONParser


class JenkinsAnalyzer:

    def __init__(self):
        self.ai = GeminiService()

    def analyze(self, pipeline_path):

        loader = JenkinsLoader(pipeline_path)

        pipeline = loader.load_pipeline()

        prompt = f"""
{JENKINS_ANALYSIS_PROMPT}

Jenkins Pipeline:

Filename:
{pipeline['filename']}

Pipeline:

{pipeline['content']}
"""

        response = self.ai.generate_response(prompt)

        return JSONParser.parse(response)
