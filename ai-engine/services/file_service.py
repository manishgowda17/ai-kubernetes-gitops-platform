from pathlib import Path


class FileService:

    @staticmethod
    def save(filename, content):

        output = Path(__file__).parent.parent / "generated"

        output.mkdir(exist_ok=True)

        file = output / filename

        file.write_text(content, encoding="utf-8")

        return filename
