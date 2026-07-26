from utils.jenkins_loader import JenkinsLoader

loader = JenkinsLoader("../Jenkinsfile")

pipeline = loader.load_pipeline()

print("=" * 60)
print(pipeline["filename"])
print("=" * 60)
print(pipeline["content"])
