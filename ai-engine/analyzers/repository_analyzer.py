import json

from analyzers.docker_analyzer import DockerAnalyzer
from analyzers.kubernetes_analyzer import KubernetesAnalyzer
from analyzers.helm_analyzer import HelmAnalyzer
from analyzers.jenkins_analyzer import JenkinsAnalyzer
from analyzers.terraform_analyzer import TerraformAnalyzer

from services.repository_scanner import RepositoryScanner
from services.gemini_service import GeminiService

from prompts.platform_prompt import PLATFORM_SUMMARY_PROMPT

from utils.json_parser import JSONParser


class RepositoryAnalyzer:

    def __init__(self, repo_path):

        self.repo_path = repo_path
        self.scanner = RepositoryScanner(repo_path)
        self.ai = GeminiService()

    def analyze(self):

        detected = self.scanner.scan()

        report = {}

        if detected["docker"]:
            report["docker"] = DockerAnalyzer().analyze(
                detected["docker"]
            )

        if detected["kubernetes"]:
            report["kubernetes"] = KubernetesAnalyzer().analyze(
                detected["kubernetes"]
            )

        if detected["helm"]:
            report["helm"] = HelmAnalyzer().analyze(
                detected["helm"]
            )

        if detected["jenkins"]:
            report["jenkins"] = JenkinsAnalyzer().analyze(
                detected["jenkins"]
            )
        
        if detected["terraform"]:
            report["terraform"] = TerraformAnalyzer().analyze(
                detected["terraform"]
            )

        prompt = f"""
{PLATFORM_SUMMARY_PROMPT}

Infrastructure Reports

{json.dumps(report, indent=4)}
"""

        summary = JSONParser.parse(
            self.ai.generate_response(prompt)
        )

        return {
            "summary": summary,
            "detailed_reports": report
        }
