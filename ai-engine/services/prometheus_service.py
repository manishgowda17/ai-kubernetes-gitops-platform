import requests


class PrometheusService:

    def __init__(self):
        self.base_url = "http://localhost:9090"

    def query(self, query):

        response = requests.get(
            f"{self.base_url}/api/v1/query",
            params={"query": query}
        )

        response.raise_for_status()

        return response.json()

    def get_cpu_usage(self):

        return self.query(
            "100 - (avg by(instance)(rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)"
        )

    def get_memory_usage(self):

        return self.query(
            "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100"
        )

    def get_container_restarts(self):

        return self.query(
            "kube_pod_container_status_restarts_total"
        )
