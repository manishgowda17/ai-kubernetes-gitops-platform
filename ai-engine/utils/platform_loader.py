from pathlib import Path


class PlatformLoader:

    def __init__(self, repo_path):
        self.repo = Path(repo_path)

    def load(self):

        files = {}

        # Docker
        docker = self.repo / "Dockerfile"
        if docker.exists():
            files["docker"] = docker.read_text()

        # Jenkins
        jenkins = self.repo / "Jenkinsfile"
        if jenkins.exists():
            files["jenkins"] = jenkins.read_text()

        # Terraform
        terraform = {}

        tf_dir = self.repo / "terraform"

        if tf_dir.exists():

            for tf in tf_dir.glob("*.tf"):
                terraform[tf.name] = tf.read_text()

            files["terraform"] = terraform

        # Kubernetes

        kubernetes = {}

        k8s = self.repo / "kubernetes"

        if k8s.exists():

            for file in k8s.glob("*.yaml"):
                kubernetes[file.name] = file.read_text()

            files["kubernetes"] = kubernetes

        # Helm

        helm = {}

        helm_dir = self.repo / "ai-platform"

        if helm_dir.exists():

            for file in helm_dir.rglob("*"):

                if file.is_file():

                    helm[str(file.relative_to(helm_dir))] = file.read_text()

            files["helm"] = helm

        return files
