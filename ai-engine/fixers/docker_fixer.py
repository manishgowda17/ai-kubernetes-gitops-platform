from fixers.base_fixer import BaseFixer
from prompts.docker_fix_prompt import DOCKER_FIX_PROMPT


class DockerFixer(BaseFixer):

    def fix(self, dockerfile_path):
        return self.fix_file(
            dockerfile_path,
            DOCKER_FIX_PROMPT
        )
