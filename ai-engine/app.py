from fastapi import FastAPI
from analyzers.docker_analyzer import DockerAnalyzer

app = FastAPI(
    title="AI Platform Engineering Copilot",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Platform Engineering Copilot"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze/docker")
def analyze_docker():

    analyzer = DockerAnalyzer()

    result = analyzer.analyze("../Dockerfile")

    return result    
