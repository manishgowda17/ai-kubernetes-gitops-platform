from utils.kubernetes_loader import KubernetesLoader

loader = KubernetesLoader("../kubernetes")

resources = loader.load_manifests()

for resource in resources:

    print("=" * 40)

    print(resource["filename"])

    print(resource["kind"])

    print(resource["metadata"])

    print("=" * 40)
