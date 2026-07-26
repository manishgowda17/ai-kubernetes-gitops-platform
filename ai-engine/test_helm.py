from analyzers.helm_analyzer import HelmAnalyzer

analyzer = HelmAnalyzer()

result = analyzer.analyze("../ai-platform")

print(result)
