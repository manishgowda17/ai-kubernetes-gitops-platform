from fixers.base_fixer import BaseFixer
from prompts.jenkins_fix_prompt import JENKINS_FIX_PROMPT


class JenkinsFixer(BaseFixer):

    def fix(self, jenkinsfile):

        return self.fix_file(
            jenkinsfile,
            JENKINS_FIX_PROMPT
        )
