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

from fastapi.responses import FileResponse
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from services.repository_service import RepositoryService
from analyzers.repository_analyzer import RepositoryAnalyzer

from analyzers.monitoring_analyzer import MonitoringAnalyzer

app = FastAPI(
    title="AI Platform Engineering Copilot",
    version="1.0.0",
    description="AI-powered DevOps Analyzer And Fixer"
)
import time

from fastapi import Request
from fastapi.responses import Response

from prometheus_client import (
    generate_latest,
    CONTENT_TYPE_LATEST
)

from services.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY
)

app = FastAPI()
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    REQUEST_COUNT.labels(
        request.method,
        request.url.path
    ).inc()

    REQUEST_LATENCY.labels(
        request.method,
        request.url.path
    ).observe(duration)

    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RepositoryRequest(BaseModel):
    repo_url: str
@app.post("/analyze/repository")
def analyze_repository(request: RepositoryRequest):

    RepositoryService.clone(request.repo_url)

    analyzer = RepositoryAnalyzer("repository")

    return analyzer.analyze()
@app.post("/fix/docker")
def fix_docker():

    fixer = DockerFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/Dockerfile"
    )

    return {
        "status": "success",
        "message": "Dockerfile generated successfully",
        "download_url": f"/download/{filename}"
    }
@app.post("/fix/kubernetes")
def fix_kubernetes():

    fixer = KubernetesFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/kubernetes"
    )

    return {
        "status": "success",
        "message": "Kubernetes manifests generated successfully",
        "download_url": f"/download/{filename}"
    }
@app.post("/fix/helm")
def fix_helm():

    fixer = HelmFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/ai-platform"
    )

    return {
        "status": "success",
        "message": "Helm chart generated successfully",
        "download_url": f"/download/{filename}"
    }
@app.post("/fix/terraform")
def fix_terraform():

    fixer = TerraformFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/terraform"
    )

    return {
        "status": "success",
        "message": "Terraform configuration generated successfully",
        "download_url": f"/download/{filename}"
    }
@app.post("/fix/jenkins")
def fix_jenkins():

    fixer = JenkinsFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/Jenkinsfile"
    )

    return {
        "status": "success",
        "message": "Jenkinsfile generated successfully",
        "download_url": f"/download/{filename}"
    }
@app.get("/download/{filename}")
def download(filename: str):

    return FileResponse(
        f"generated/{filename}",
        filename=filename
    )
@app.get("/download/{filename}")
def download(filename: str):

    file = Path(__file__).parent / "generated" / filename

    if not file.exists():
        raise HTTPException(
            status_code=404,
            detail=f"{filename} not found"
        )

    return FileResponse(
        path=file,
        filename=file.name,
        media_type="application/octet-stream"
    )
@app.post("/fix/all")
def fix_all():

    docker = DockerFixer().fix(f"{REPOSITORY_PATH}/Dockerfile")

    terraform = TerraformFixer().fix(f"{REPOSITORY_PATH}/terraform")

    kubernetes = KubernetesFixer().fix(f"{REPOSITORY_PATH}/k8s")

    helm = HelmFixer().fix(f"{REPOSITORY_PATH}/helm")

    jenkins = JenkinsFixer().fix(f"{REPOSITORY_PATH}/Jenkinsfile")

    return {
        "message": "All fixes generated successfully"
    }
@app.get("/")
def home():
    return {"message": "Hello"}

@app.post("/analyze/repository")
def analyze_repository():
    ...

@app.post("/fix/docker")
def fix_docker():
    ...

@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
@app.get("/analyze/monitoring")
def analyze_monitoring():

    analyzer = MonitoringAnalyzer()

    return analyzer.analyze(@app.get("/incident/report")
def incident_report():

    analyzer = MonitoringAnalyzer()

    return analyzer.analyze()

