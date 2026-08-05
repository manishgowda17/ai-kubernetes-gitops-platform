class IncidentDetector:

    def detect(self, cpu, memory, restarts):

        incidents = []

        if cpu > 90:
            incidents.append("High CPU Usage")

        if memory > 85:
            incidents.append("High Memory Usage")

        if restarts > 5:
            incidents.append("Frequent Container Restarts")

        return incidents
