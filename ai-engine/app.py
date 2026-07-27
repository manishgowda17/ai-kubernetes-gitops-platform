from fastapi import FastAPI

from config import REPOSITORY_PATH

from analyzers.docker_analyzer import DockerAnalyzer
from analyzers.kubernetes_analyzer import KubernetesAnalyzer
from analyzers.helm_analyzer import HelmAnalyzer
from analyzers.jenkins_analyzer import JenkinsAnalyzer
from analyzers.repository_analyzer import RepositoryAnalyzer

app = FastAPI(
    title="AI Platform Engineering Copilot",
    version="1.0.0",
    description="AI-powered DevOps and Kubernetes Analyzer"
)


@app.get("/")
def home():
    return {
        "message": "AI Platform Engineering Copilot",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze/docker")
def analyze_docker():

    analyzer = DockerAnalyzer()

    return analyzer.analyze(f"{REPOSITORY_PATH}/Dockerfile")


@app.post("/analyze/kubernetes")
def analyze_kubernetes():

    analyzer = KubernetesAnalyzer()

    return analyzer.analyze(f"{REPOSITORY_PATH}/kubernetes")

@app.post("/analyze/helm")
def analyze_helm():

    analyzer = HelmAnalyzer()

    return analyzer.analyze(f"{REPOSITORY_PATH}/ai-platform")

@app.post("/analyze/jenkins")
def analyze_jenkins():

    analyzer = JenkinsAnalyzer()

    return analyzer.analyze(f"{REPOSITORY_PATH}/Jenkinsfile")
@app.post("/analyze/repository")
def analyze_repository():

    analyzer = RepositoryAnalyzer(REPOSITORY_PATH)

    return analyzer.analyze()
