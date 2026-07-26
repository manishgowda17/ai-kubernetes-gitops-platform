from fastapi import FastAPI

from analyzers.docker_analyzer import DockerAnalyzer
from analyzers.kubernetes_analyzer import KubernetesAnalyzer
from analyzers.helm_analyzer import HelmAnalyzer

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

    return analyzer.analyze("../Dockerfile")


@app.post("/analyze/kubernetes")
def analyze_kubernetes():

    analyzer = KubernetesAnalyzer()

    return analyzer.analyze("../kubernetes")
@app.post("/analyze/helm")
def analyze_helm():

    analyzer = HelmAnalyzer()

    return analyzer.analyze("../ai-platform")
