import time
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel

from prometheus_client import (
    CONTENT_TYPE_LATEST,
    generate_latest,
)

from config import REPOSITORY_PATH

from services.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY,
)

from services.repository_service import RepositoryService

from analyzers.docker_analyzer import DockerAnalyzer
from analyzers.kubernetes_analyzer import KubernetesAnalyzer
from analyzers.helm_analyzer import HelmAnalyzer
from analyzers.jenkins_analyzer import JenkinsAnalyzer
from analyzers.repository_analyzer import RepositoryAnalyzer
from analyzers.monitoring_analyzer import MonitoringAnalyzer
from analyzers.kubernetes_live_analyzer import KubernetesLiveAnalyzer

from fixers.docker_fixer import DockerFixer
from fixers.kubernetes_fixer import KubernetesFixer
from fixers.terraform_fixer import TerraformFixer
from fixers.helm_fixer import HelmFixer
from fixers.jenkins_fixer import JenkinsFixer


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="AI Platform Engineering Copilot",
    version="1.0.0",
    description="AI-powered DevOps Analyzer and Fixer",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# PROMETHEUS REQUEST METRICS
# ============================================================

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    REQUEST_COUNT.labels(
        request.method,
        request.url.path,
    ).inc()

    REQUEST_LATENCY.labels(
        request.method,
        request.url.path,
    ).observe(duration)

    return response


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "AI Platform Engineering Copilot",
        "version": "1.0.0",
        "status": "running",
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
    }


# ============================================================
# REPOSITORY ANALYSIS
# ============================================================

class RepositoryRequest(BaseModel):
    repo_url: str


@app.post("/analyze/repository")
def analyze_repository(request: RepositoryRequest):

    RepositoryService.clone(request.repo_url)

    analyzer = RepositoryAnalyzer("repository")

    return analyzer.analyze()


# ============================================================
# DOCKER ANALYSIS
# ============================================================

@app.post("/analyze/docker")
def analyze_docker():

    analyzer = DockerAnalyzer()

    return analyzer.analyze(
        f"{REPOSITORY_PATH}/Dockerfile"
    )


# ============================================================
# KUBERNETES ANALYSIS
# ============================================================

@app.post("/analyze/kubernetes")
def analyze_kubernetes():

    analyzer = KubernetesAnalyzer()

    return analyzer.analyze(
        f"{REPOSITORY_PATH}/kubernetes"
    )


# ============================================================
# HELM ANALYSIS
# ============================================================

@app.post("/analyze/helm")
def analyze_helm():

    analyzer = HelmAnalyzer()

    return analyzer.analyze(
        f"{REPOSITORY_PATH}/ai-platform"
    )


# ============================================================
# JENKINS ANALYSIS
# ============================================================

@app.post("/analyze/jenkins")
def analyze_jenkins():

    analyzer = JenkinsAnalyzer()

    return analyzer.analyze(
        f"{REPOSITORY_PATH}/Jenkinsfile"
    )


# ============================================================
# DOCKER FIX
# ============================================================

@app.post("/fix/docker")
def fix_docker():

    fixer = DockerFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/Dockerfile"
    )

    return {
        "status": "success",
        "message": "Dockerfile generated successfully",
        "download_url": f"/download/{filename}",
    }


# ============================================================
# KUBERNETES FIX
# ============================================================

@app.post("/fix/kubernetes")
def fix_kubernetes():

    fixer = KubernetesFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/kubernetes"
    )

    return {
        "status": "success",
        "message": "Kubernetes manifests generated successfully",
        "download_url": f"/download/{filename}",
    }


# ============================================================
# TERRAFORM FIX
# ============================================================

@app.post("/fix/terraform")
def fix_terraform():

    fixer = TerraformFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/terraform"
    )

    return {
        "status": "success",
        "message": "Terraform configuration generated successfully",
        "download_url": f"/download/{filename}",
    }


# ============================================================
# HELM FIX
# ============================================================

@app.post("/fix/helm")
def fix_helm():

    fixer = HelmFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/ai-platform"
    )

    return {
        "status": "success",
        "message": "Helm chart generated successfully",
        "download_url": f"/download/{filename}",
    }


# ============================================================
# JENKINS FIX
# ============================================================

@app.post("/fix/jenkins")
def fix_jenkins():

    fixer = JenkinsFixer()

    filename = fixer.fix(
        f"{REPOSITORY_PATH}/Jenkinsfile"
    )

    return {
        "status": "success",
        "message": "Jenkinsfile generated successfully",
        "download_url": f"/download/{filename}",
    }


# ============================================================
# GENERATE ALL FIXES
# ============================================================

@app.post("/fix/all")
def fix_all():

    DockerFixer().fix(
        f"{REPOSITORY_PATH}/Dockerfile"
    )

    TerraformFixer().fix(
        f"{REPOSITORY_PATH}/terraform"
    )

    KubernetesFixer().fix(
        f"{REPOSITORY_PATH}/kubernetes"
    )

    HelmFixer().fix(
        f"{REPOSITORY_PATH}/ai-platform"
    )

    JenkinsFixer().fix(
        f"{REPOSITORY_PATH}/Jenkinsfile"
    )

    return {
        "status": "success",
        "message": "All fixes generated successfully",
    }


# ============================================================
# DOWNLOAD GENERATED FILES
# ============================================================

@app.get("/download/{filename}")
def download(filename: str):

    generated_dir = Path(__file__).parent / "generated"
    file = generated_dir / filename

    if not file.exists():
        raise HTTPException(
            status_code=404,
            detail=f"{filename} not found",
        )

    return FileResponse(
        path=file,
        filename=file.name,
        media_type="application/octet-stream",
    )


# ============================================================
# PROMETHEUS METRICS
# ============================================================

@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )


# ============================================================
# MONITORING ANALYSIS
# ============================================================

@app.get("/analyze/monitoring")
def analyze_monitoring():

    analyzer = MonitoringAnalyzer()

    return analyzer.analyze()


# ============================================================
# INCIDENT REPORT
# ============================================================

@app.get("/incident/report")
def incident_report():

    analyzer = MonitoringAnalyzer()

    return analyzer.analyze()


# ============================================================
# LIVE KUBERNETES ANALYSIS
# ============================================================

@app.get("/analyze/kubernetes/live")
def analyze_live_cluster():

    analyzer = KubernetesLiveAnalyzer()

    return analyzer.analyze()
