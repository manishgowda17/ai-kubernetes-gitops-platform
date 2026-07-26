from pathlib import Path


class JenkinsLoader:

    def __init__(self, jenkinsfile_path):
        self.jenkinsfile_path = Path(jenkinsfile_path)

    def load_pipeline(self):

        if not self.jenkinsfile_path.exists():
            raise FileNotFoundError(
                f"{self.jenkinsfile_path} not found."
            )

        return {
            "filename": self.jenkinsfile_path.name,
            "content": self.jenkinsfile_path.read_text()
        }
