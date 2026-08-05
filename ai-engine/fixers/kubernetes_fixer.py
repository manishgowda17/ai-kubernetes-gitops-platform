from fixers.base_fixer import BaseFixer
from prompts.kubernetes_fix_prompt import KUBERNETES_FIX_PROMPT
from services.file_service import FileService


class KubernetesFixer(BaseFixer):

    def fix(self, kubernetes_folder):

        fixed = self.fix_file(
            kubernetes_folder,
            KUBERNETES_FIX_PROMPT
        )

        return FileService.save(
            "deployment.fixed.yaml",
            fixed
        )
