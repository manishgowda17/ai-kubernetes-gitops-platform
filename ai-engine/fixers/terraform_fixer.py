from fixers.base_fixer import BaseFixer
from prompts.terraform_fix_prompt import TERRAFORM_FIX_PROMPT
from services.file_service import FileService


class TerraformFixer(BaseFixer):

    def fix(self, terraform_folder):

        fixed = self.fix_file(
            terraform_folder,
            TERRAFORM_FIX_PROMPT
        )

        filename = FileService.save(
            "main.fixed.tf",
            fixed
        )

        return filename
