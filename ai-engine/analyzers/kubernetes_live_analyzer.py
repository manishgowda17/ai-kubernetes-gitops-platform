from services.kubernetes_service import KubernetesService
from services.gemini_service import GeminiService


class KubernetesLiveAnalyzer:

    def __init__(self):

        self.k8s = KubernetesService()

        self.ai = GeminiService()

    def analyze(self):

        pods = self.k8s.get_pods()

        nodes = self.k8s.get_nodes()

        prompt = f"""
You are a Senior Kubernetes Platform Engineer.

Analyze this cluster.

Pods

{pods}

Nodes

{nodes}

Provide

1. Cluster Health

2. Risks

3. Root Cause

4. Recommendations
"""

        return self.ai.generate_response(prompt)
