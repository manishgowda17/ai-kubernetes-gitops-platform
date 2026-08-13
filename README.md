# 🚀 AI Platform Engineering Copilot

An **AI-powered DevOps and Platform Engineering assistant** that analyzes repositories, evaluates cloud-native infrastructure, identifies security and reliability issues, generates fixes, and monitors live Kubernetes environments.

The project combines **FastAPI, Docker, Kubernetes, Helm, Terraform, Jenkins, Prometheus, Grafana, Node Exporter, cAdvisor, and AI-powered analysis** into a single platform.

---

## 📌 Overview

Modern DevOps environments involve multiple technologies and configuration files. Reviewing all of them manually can be time-consuming and error-prone.

The **AI Platform Engineering Copilot** provides a centralized platform to:

* Analyze DevOps repositories
* Detect infrastructure and security issues
* Score different components
* Generate recommended fixes
* Analyze live Kubernetes clusters
* Monitor infrastructure using Prometheus
* Visualize metrics using Grafana
* Generate incident-oriented reports
* Provide a simple DevOps dashboard

The goal is to demonstrate practical experience with **Platform Engineering, DevOps, Kubernetes, Infrastructure as Code, CI/CD, observability, and cloud security**.

---

# ✨ Features

## 🔍 Repository Analysis

Users can provide a GitHub repository URL and analyze the repository without manually uploading individual files.

Example:

```text
https://github.com/manishgowda17/ai-kubernetes-gitops-platform
```

The system clones the repository and analyzes its infrastructure configuration.

### Repository analysis includes:

* Architecture score
* Security score
* Maintainability score
* Production-readiness score
* Infrastructure issues
* Security issues
* Recommendations

---

# 🐳 Docker Analysis

Analyzes Docker configuration and identifies common containerization problems.

### Checks include:

* Dockerfile configuration
* `.dockerignore`
* Container security
* Image configuration
* Security-related container settings
* Container best practices

Example output:

```json
{
  "score": 88,
  "issues": [
    "Missing .dockerignore",
    "Container security options are not explicitly configured"
  ]
}
```

---

# ☸️ Kubernetes Analysis

Analyzes Kubernetes manifests and detects configuration and security problems.

### Checks include:

* Deployments
* Services
* Ingress
* Secrets
* NetworkPolicies
* Image tags
* Security configuration
* Production readiness

Examples of detected issues:

* Hardcoded secrets
* Mutable `latest` image tags
* Incorrect NetworkPolicies
* Missing TLS configuration
* Insecure Kubernetes configuration

---

# ⎈ Helm Analysis

Analyzes Helm charts and their configuration.

### Checks include:

* `values.yaml`
* Container images
* Service ports
* Target ports
* Resource limits
* Security contexts
* Pod security configuration
* Application-specific configuration

---

# 🏗️ Terraform Analysis

Analyzes Infrastructure as Code configurations.

### Checks include:

* AWS security groups
* EC2 configuration
* S3 configuration
* Public exposure
* Encryption
* Versioning
* AMI configuration
* Terraform state configuration
* Network architecture

Example issues:

```text
SSH open to 0.0.0.0/0
S3 encryption not configured
S3 versioning disabled
Hardcoded AMI ID
Missing remote state backend
```

---

# 🔧 Jenkins Analysis

Analyzes Jenkins CI/CD configuration.

The analyzer can identify problems related to:

* Jenkinsfile configuration
* CI/CD automation
* Pipeline structure
* Deployment automation
* Production readiness

---

# 🤖 AI-Generated Fixes

The platform can generate fixes for supported DevOps configurations.

Supported fixers include:

* Docker
* Kubernetes
* Terraform
* Helm
* Jenkins

Generated files can be downloaded from the backend.

Example API response:

```json
{
  "status": "success",
  "message": "Dockerfile generated successfully",
  "download_url": "/download/generated-file"
}
```

---

# ☸️ Live Kubernetes Cluster Analysis

The platform can analyze a running Kubernetes cluster.

It provides information about the live cluster and helps identify operational issues.

Example:

```bash
kubectl get nodes
```

The backend communicates with the Kubernetes API using the Kubernetes Python client.

This demonstrates practical experience with:

* Kubernetes API
* Cluster inspection
* Node analysis
* Workload analysis
* Kubernetes operations

---

# 📊 Monitoring & Observability

The project includes a complete monitoring stack using:

* Prometheus
* Grafana
* Node Exporter
* cAdvisor

### Architecture

```text
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │                      │
                    │ Monitoring Analyzer  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Prometheus      │
                    │                      │
                    │ Metrics Collection   │
                    └──────┬─────────┬─────┘
                           │         │
                ┌──────────┘         └──────────┐
                ▼                               ▼
        ┌───────────────┐              ┌───────────────┐
        │ Node Exporter │              │    cAdvisor   │
        │ Host Metrics  │              │Container Stats│
        └───────────────┘              └───────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Grafana    │
                    │ Visualization│
                    └──────────────┘
```

---

# 📈 Prometheus

Prometheus collects infrastructure and application metrics.

Configured monitoring targets include:

```text
Prometheus
Node Exporter
cAdvisor
FastAPI
```

The FastAPI application also exposes:

```text
/metrics
```

for Prometheus scraping.

---

# 📊 Grafana

Grafana is used to visualize infrastructure metrics.

The monitoring stack can be used to observe:

* CPU usage
* Memory usage
* Container metrics
* Host metrics
* Application metrics
* Infrastructure health

---

# 🖥️ Node Exporter

Node Exporter collects host-level system metrics.

Examples:

* CPU
* Memory
* Disk
* Network
* System statistics

---

# 📦 cAdvisor

cAdvisor provides container-level metrics.

It allows monitoring of:

* Docker containers
* CPU usage
* Memory usage
* Container resource consumption
* Container performance

---

# 🚨 Incident Reporting

The platform includes an incident-reporting endpoint based on monitoring information.

The purpose is to provide a centralized view of infrastructure issues detected from the monitoring system.

Example endpoint:

```text
GET /incident/report
```

---

# 🌐 Frontend

The frontend is intentionally lightweight.

Instead of using a large frontend framework, the dashboard is built using:

* HTML
* CSS
* JavaScript

The dashboard follows a **dark DevOps dashboard design** with a sidebar and sections for different platform capabilities.

### Dashboard capabilities

* Repository analysis
* Docker analysis
* Kubernetes analysis
* Helm analysis
* Jenkins analysis
* Terraform fixes
* Live Kubernetes analysis
* Monitoring analysis
* Incident reports
* AI-generated fixes

---

# ⚙️ Backend

The backend is built using **FastAPI**.

Main responsibilities include:

* API endpoints
* Repository cloning
* Infrastructure analysis
* Fix generation
* Kubernetes integration
* Prometheus integration
* Metrics exposure
* File downloads
* CORS handling

---

# 🔌 API Endpoints

## Health

```http
GET /
```

```http
GET /health
```

---

## Repository

```http
POST /analyze/repository
```

Request:

```json
{
  "repo_url": "https://github.com/user/repository"
}
```

---

## Infrastructure Analysis

```http
POST /analyze/docker
```

```http
POST /analyze/kubernetes
```

```http
POST /analyze/helm
```

```http
POST /analyze/jenkins
```

---

## Monitoring

```http
GET /analyze/monitoring
```

---

## Live Kubernetes

```http
GET /analyze/kubernetes/live
```

---

## Incident Report

```http
GET /incident/report
```

---

## Prometheus Metrics

```http
GET /metrics
```

---

## Fix Generation

```http
POST /fix/docker
```

```http
POST /fix/kubernetes
```

```http
POST /fix/terraform
```

```http
POST /fix/helm
```

```http
POST /fix/jenkins
```

---

# 🏗️ Project Structure

```text
ai-platform-copilot/
│
├── ai-engine/
│   │
│   ├── app.py
│   ├── main.py
│   ├── config.py
│   │
│   ├── analyzers/
│   │   ├── docker_analyzer.py
│   │   ├── kubernetes_analyzer.py
│   │   ├── helm_analyzer.py
│   │   ├── jenkins_analyzer.py
│   │   ├── repository_analyzer.py
│   │   ├── monitoring_analyzer.py
│   │   └── kubernetes_live_analyzer.py
│   │
│   ├── fixers/
│   │   ├── docker_fixer.py
│   │   ├── kubernetes_fixer.py
│   │   ├── terraform_fixer.py
│   │   ├── helm_fixer.py
│   │   └── jenkins_fixer.py
│   │
│   ├── services/
│   │   ├── repository_service.py
│   │   ├── prometheus_service.py
│   │   ├── kubernetes_service.py
│   │   └── metrics.py
│   │
│   └── generated/
│
├── monitoring/
│   │
│   ├── docker-compose.yml
│   │
│   ├── prometheus/
│   │   └── prometheus.yml
│   │
│   ├── grafana/
│   │
│   └── loki/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# 🛠️ Technologies Used

| Technology          | Purpose                       |
| ------------------- | ----------------------------- |
| Python              | Backend and automation        |
| FastAPI             | REST API                      |
| Google Gemini       | AI-powered analysis           |
| Docker              | Containerization              |
| Kubernetes          | Container orchestration       |
| Helm                | Kubernetes package management |
| Terraform           | Infrastructure as Code        |
| Jenkins             | CI/CD                         |
| Prometheus          | Metrics collection            |
| Grafana             | Monitoring visualization      |
| Node Exporter       | Host metrics                  |
| cAdvisor            | Container metrics             |
| GitPython           | Repository cloning            |
| HTML/CSS/JavaScript | Frontend dashboard            |
| AWS                 | Cloud infrastructure          |

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/manishgowda17/ai-kubernetes-gitops-platform.git
cd ai-kubernetes-gitops-platform
```

---

# 🐍 Backend Setup

Move into the backend:

```bash
cd ai-engine
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If a requirements file is not available:

```bash
pip install fastapi uvicorn python-dotenv prometheus-client google-genai pydantic requests gitpython kubernetes
```

---

# 🔐 Environment Variables

Create a `.env` file inside the backend configuration location required by the project.

Example:

```env
GEMINI_API_KEY=your_api_key
```

Do **not** commit API keys or secrets to GitHub.

Add `.env` to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

---

# ▶️ Start the Backend

```bash
python3 main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 📊 Start Monitoring Stack

Move into the monitoring directory:

```bash
cd monitoring
```

Start the services:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

Expected services include:

```text
prometheus
grafana
node-exporter
cadvisor
```

---

# 🔎 Monitoring URLs

Prometheus:

```text
http://localhost:9090
```

Grafana:

```text
http://localhost:3000
```

cAdvisor:

```text
http://localhost:8080
```

Node Exporter:

```text
http://localhost:9100
```

FastAPI metrics:

```text
http://localhost:8000/metrics
```

---

# 🧪 Testing the API

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Monitoring:

```bash
curl http://127.0.0.1:8000/analyze/monitoring
```

Live Kubernetes:

```bash
curl http://127.0.0.1:8000/analyze/kubernetes/live
```

Incident report:

```bash
curl http://127.0.0.1:8000/incident/report
```

Metrics:

```bash
curl http://127.0.0.1:8000/metrics
```

---

# 🔄 High-Level Architecture

```text
                         USER
                           │
                           ▼
                ┌────────────────────┐
                │  DevOps Dashboard  │
                │ HTML/CSS/JavaScript │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │      FastAPI       │
                │       API          │
                └─────────┬──────────┘
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
   Repository        Infrastructure     Monitoring
    Analysis            Analysis          Analysis
          │               │                │
          │       ┌───────┼────────┐       │
          │       │       │        │       │
          ▼       ▼       ▼        ▼       ▼
        Git    Docker Kubernetes Helm  Prometheus
                Terraform Jenkins       │
                                        │
                           ┌────────────┼───────────┐
                           ▼            ▼           ▼
                       Node Exporter cAdvisor    FastAPI
                           │            │           │
                           └────────────┼───────────┘
                                        ▼
                                    Grafana
```

---

# 🎯 Project Goals

This project was built to demonstrate practical Platform Engineering and DevOps capabilities across the complete infrastructure lifecycle:

```text
Code
 ↓
Containerization
 ↓
Infrastructure as Code
 ↓
Kubernetes
 ↓
Helm
 ↓
CI/CD
 ↓
Monitoring
 ↓
Observability
 ↓
Incident Analysis
 ↓
AI-assisted Remediation
```

---

# 🔐 Security Considerations

The platform is designed with security analysis as one of its core capabilities.

It can identify issues such as:

* Hardcoded secrets
* Publicly exposed infrastructure
* Insecure container configurations
* Mutable container image tags
* Missing encryption
* Missing Kubernetes TLS
* Overly permissive security groups
* Insecure Kubernetes configurations

Generated recommendations can then be used to improve the infrastructure configuration.

> **Important:** Generated fixes should always be reviewed before being applied to production infrastructure.

---

# 📚 What This Project Demonstrates

This project demonstrates hands-on experience with:

### DevOps

* CI/CD
* Jenkins
* Docker
* Linux
* Git
* Automation

### Cloud

* AWS
* EC2
* S3
* IAM
* Infrastructure security

### Kubernetes

* Kubernetes manifests
* Deployments
* Services
* Ingress
* Secrets
* NetworkPolicies
* Helm
* Kubernetes API
* Live cluster analysis

### Infrastructure as Code

* Terraform
* AWS infrastructure
* State management
* Infrastructure security

### Observability

* Prometheus
* Grafana
* Node Exporter
* cAdvisor
* Application metrics
* Incident analysis

### AI

* AI-assisted DevOps analysis
* Infrastructure recommendations
* Automated configuration fixes
* Repository analysis

---

# 🚧 Future Improvements

Potential future enhancements include:

* GitHub Actions integration
* Automated security scanning
* Trivy integration
* SonarQube integration
* Argo CD / GitOps deployment
* Alertmanager integration
* Slack/Discord incident notifications
* More advanced AI remediation
* Multi-cloud support
* Authentication and role-based access
* Persistent analysis history
* Production-grade secrets management

---

# ⭐ Why This Project?

The project was built as a practical Platform Engineering project rather than a simple CRUD application.

It brings together:

**AI + DevOps + Kubernetes + Cloud + IaC + CI/CD + Observability**

into one platform to demonstrate how modern infrastructure can be analyzed, monitored, and improved using automation and AI.

---

## 📄 License

This project is intended for educational, experimentation, and portfolio purposes.

