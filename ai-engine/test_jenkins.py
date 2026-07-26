from analyzers.jenkins_analyzer import JenkinsAnalyzer

analyzer = JenkinsAnalyzer()

result = analyzer.analyze("../Jenkinsfile")

print(result)
