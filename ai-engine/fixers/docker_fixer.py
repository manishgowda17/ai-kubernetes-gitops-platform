from fixers.base_fixer import BaseFixer
from prompts.docker_fix_prompt import DOCKER_FIX_PROMPT
from services.file_service import FileService


class DockerFixer(BaseFixer):

    def fix(self, dockerfile):

        fixed = self.fix_file(
            dockerfile,
            DOCKER_FIX_PROMPT
        )

        path = FileService.save(
            "Dockerfile.fixed",
            fixed
        )

        return path
