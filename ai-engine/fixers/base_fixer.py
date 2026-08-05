from pathlib import Path

from services.gemini_service import GeminiService


class BaseFixer:

    def __init__(self):
        self.ai = GeminiService()

    def fix_file(self, path, prompt):

        path = Path(path)

        content = ""

        if path.is_file():

            content = path.read_text(encoding="utf-8")

        elif path.is_dir():

            for file in path.rglob("*"):

                if file.suffix in [".tf", ".yaml", ".yml"] or file.name == "Chart.yaml":

                    content += f"\n\n===== {file.name} =====\n\n"

                    content += file.read_text(encoding="utf-8")

        full_prompt = f"""
{prompt}

Infrastructure Files

{content}
"""

        return self.ai.generate_response(full_prompt)
