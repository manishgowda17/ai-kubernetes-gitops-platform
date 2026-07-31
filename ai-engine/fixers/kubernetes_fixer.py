from pathlib import Path

from fixers.base_fixer import BaseFixer
from prompts.kubernetes_fix_prompt import KUBERNETES_FIX_PROMPT


class KubernetesFixer(BaseFixer):

    def fix(self, kubernetes_folder):

        yaml = ""

        for file in Path(kubernetes_folder).glob("*.yaml"):
            yaml += file.read_text() + "\n\n"

        prompt = f"""
{KUBERNETES_FIX_PROMPT}

{yaml}
"""

        return self.ai.generate_response(prompt)
