from utils.helm_loader import HelmLoader

loader = HelmLoader("../ai-platform")

files = loader.load_chart()

for file in files:

    print("=" * 40)

    print(file["filename"])

    print("=" * 40)

    print(file["content"][:200])

    print()
