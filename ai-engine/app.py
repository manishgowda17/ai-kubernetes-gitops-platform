from fastapi import FastAPI

from config import REPOSITORY_PATH

from analyzers.docker_analyzer import DockerAnalyzer
from analyzers.kubernetes_analyzer import KubernetesAnalyzer
from analyzers.helm_analyzer import HelmAnalyzer
from analyzers.jenkins_analyzer import JenkinsAnalyzer
from analyzers.repository_analyzer import RepositoryAnalyzer

from fixers.docker_fixer import DockerFixer
from fixers.kubernetes_fixer import KubernetesFixer
from fixers.terraform_fixer import TerraformFixer
from fixers.helm_fixer import HelmFixer
from fixers.jenkins_fixer import JenkinsFixer

app = FastAPI(
    title="AI Platform Engineering Copilot",
    version="1.0.0",
    description="AI-powered DevOps Analyzer And Fixer"
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
@app.post("/fix/docker")
def fix_docker():

    fixer = DockerFixer()

    return {
        "fixed_dockerfile":
            fixer.fix(f"{REPOSITORY_PATH}/Dockerfile")
    }
@app.post("/fix/kubernetes")
def fix_kubernetes():

    fixer = KubernetesFixer()

    return {
        "fixed_yaml":
            fixer.fix(f"{REPOSITORY_PATH}/kubernetes")
    }
@app.post("/fix/terraform")
def fix_terraform():

    fixer = TerraformFixer()

    return {
        "fixed_terraform":
            fixer.fix(f"{REPOSITORY_PATH}/terraform")
    }
@app.post("/fix/helm")
def fix_helm():

    fixer = HelmFixer()

    return {
        "fixed_helm":
            fixer.fix(f"{REPOSITORY_PATH}/ai-platform")
    }
@app.post("/fix/jenkins")
def fix_jenkins():

    fixer = JenkinsFixer()

    return {
        "fixed_pipeline":
            fixer.fix(f"{REPOSITORY_PATH}/Jenkinsfile")
    }
