from pathlib import Path
import yaml


class KubernetesLoader:

    def __init__(self, directory):
        self.directory = Path(directory)

    def load_manifests(self):

        manifests = []

        yaml_files = list(self.directory.glob("*.yaml"))
        yaml_files += list(self.directory.glob("*.yml"))

        for file in sorted(yaml_files):

            content = file.read_text()

            documents = list(yaml.safe_load_all(content))

            for doc in documents:

                if not doc:
                    continue

                manifests.append(
                    {
                        "filename": file.name,
                        "kind": doc.get("kind", "Unknown"),
                        "apiVersion": doc.get("apiVersion", ""),
                        "metadata": doc.get("metadata", {}),
                        "content": content
                    }
                )

        return manifests
