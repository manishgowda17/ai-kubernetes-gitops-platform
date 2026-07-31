from pathlib import Path

from services.gemini_service import GeminiService


class BaseFixer:

    def __init__(self):
        self.ai = GeminiService()

    def fix_file(self, file_path, prompt):

        content = Path(file_path).read_text()

        full_prompt = f"""
{prompt}

File Content

{content}
"""

        return self.ai.generate_response(full_prompt)
