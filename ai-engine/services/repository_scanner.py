from pathlib import Path


class RepositoryScanner:

    def __init__(self, repo_path):
        self.repo = Path(repo_path)

    def scan(self):

        detected = {
            "docker": None,
            "kubernetes": None,
            "helm": None,
            "jenkins": None,
            "terraform":None,
        }

        docker = self.repo / "Dockerfile"

        if docker.exists():
            detected["docker"] = docker

        kubernetes = self.repo / "kubernetes"

        if kubernetes.exists():
            detected["kubernetes"] = kubernetes

        helm = self.repo / "ai-platform"

        if helm.exists():
            detected["helm"] = helm

        jenkins = self.repo / "Jenkinsfile"

        if jenkins.exists():
            detected["jenkins"] = jenkins

        terraform = self.repo / "terraform"

        if terraform.exists():
            detected["terraform"] = terraform

        return detected
