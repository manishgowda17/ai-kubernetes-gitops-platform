from services.gemini_service import GeminiService
from prompts.kubernetes_prompt import KUBERNETES_ANALYSIS_PROMPT
from utils.kubernetes_loader import KubernetesLoader
from utils.json_parser import JSONParser


class KubernetesAnalyzer:

    def __init__(self):
        self.ai = GeminiService()

    def analyze(self, directory):

        loader = KubernetesLoader(directory)

        manifests = loader.load_manifests()

        combined_yaml = ""

        for manifest in manifests:

            combined_yaml += f"""

File: {manifest['filename']}

Kind: {manifest['kind']}

Content:

{manifest['content']}

------------------------------------

"""

        prompt = f"""
{KUBERNETES_ANALYSIS_PROMPT}

Kubernetes Manifests:

{combined_yaml}
"""

        response = self.ai.generate_response(prompt)

        return JSONParser.parse(response)
