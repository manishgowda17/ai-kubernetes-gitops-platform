from services.prometheus_service import PrometheusService
from services.gemini_service import GeminiService


class MonitoringAnalyzer:

    def __init__(self):

        self.prometheus = PrometheusService()
        self.ai = GeminiService()

    def analyze(self):

        cpu = self.prometheus.get_cpu_usage()

        memory = self.prometheus.get_memory_usage()

        restarts = self.prometheus.get_container_restarts()

        prompt = f"""
You are a Senior Platform Engineer.

Analyze the following Prometheus metrics.

CPU:

{cpu}

Memory:

{memory}

Container Restarts:

{restarts}

Provide:

1. Health Summary

2. Risks

3. Recommendations

4. Production Improvements
"""

        return self.ai.generate_response(prompt)
