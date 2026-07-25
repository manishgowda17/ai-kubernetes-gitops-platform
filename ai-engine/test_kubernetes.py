from analyzers.kubernetes_analyzer import KubernetesAnalyzer

analyzer = KubernetesAnalyzer()

result = analyzer.analyze("../kubernetes")

print(result)
