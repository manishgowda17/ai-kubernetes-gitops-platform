from fixers.base_fixer import BaseFixer
from prompts.jenkins_fix_prompt import JENKINS_FIX_PROMPT
from services.file_service import FileService


class JenkinsFixer(BaseFixer):

    def fix(self, jenkinsfile_path):

        fixed = self.fix_file(
            jenkinsfile_path,
            JENKINS_FIX_PROMPT
        )

        return FileService.save(
            "Jenkinsfile.fixed",
            fixed
        )
