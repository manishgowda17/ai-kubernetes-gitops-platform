import shutil
import subprocess
from pathlib import Path


class RepositoryService:

    @staticmethod
    def clone(repo_url):

        repo = Path("repository")

        if repo.exists():

            shutil.rmtree(repo)

        subprocess.run([
            "git",
            "clone",
            repo_url,
            str(repo)
        ], check=True)

        return repo
