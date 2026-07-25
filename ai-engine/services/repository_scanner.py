from pathlib import Path


class RepositoryScanner:
    """
    Scans the repository and detects DevOps-related files.
    """

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)

    def scan(self):
        detected = {
            "docker": [],
            "kubernetes": [],
            "helm": [],
            "jenkins": []
        }

        for file in self.repo_path.rglob("*"):

            if not file.is_file():
                continue

            name = file.name.lower()

            # Docker
            if name == "dockerfile":
                detected["docker"].append(str(file))

            elif name in ("docker-compose.yml", "docker-compose.yaml"):
                detected["docker"].append(str(file))

            # Kubernetes
            elif file.suffix in (".yaml", ".yml") and "kubernetes" in str(file):
                detected["kubernetes"].append(str(file))

            # Helm
            elif "ai-platform" in str(file):
                detected["helm"].append(str(file))

            # Jenkins
            elif name == "jenkinsfile":
                detected["jenkins"].append(str(file))

        return detected
