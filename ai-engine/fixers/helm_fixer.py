from fixers.base_fixer import BaseFixer
from prompts.helm_fix_prompt import HELM_FIX_PROMPT
from services.file_service import FileService


class HelmFixer(BaseFixer):

    def fix(self, helm_folder):

        fixed = self.fix_file(
            helm_folder,
            HELM_FIX_PROMPT
        )

        return FileService.save(
            "helm.fixed.yaml",
            fixed
        )
