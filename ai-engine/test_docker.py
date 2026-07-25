from analyzers.docker_analyzer import DockerAnalyzer

analyzer = DockerAnalyzer()

result = analyzer.analyze("../Dockerfile")

print(result)
