from services.repository_scanner import RepositoryScanner

scanner = RepositoryScanner("../")

files = scanner.scan()

print(files)
