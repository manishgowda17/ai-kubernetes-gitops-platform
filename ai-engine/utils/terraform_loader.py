from pathlib import Path


class TerraformLoader:

    @staticmethod
    def load(terraform_path):

        terraform_path = Path(terraform_path)

        tf_content = ""

        for file in sorted(terraform_path.glob("*.tf")):
            tf_content += f"\n===== {file.name} =====\n"
            tf_content += file.read_text()
            tf_content += "\n"

        return tf_content
