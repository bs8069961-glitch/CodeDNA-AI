from pathlib import Path


class RepositoryScanner:
    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)

    def get_python_files(self):
        python_files = []

        for file in self.repo_path.rglob("*.py"):
            if file.is_file():
                python_files.append(file)

        return sorted(python_files)


if __name__ == "__main__":
    scanner = RepositoryScanner(".")
    files = scanner.get_python_files()

    print(f"\nFound {len(files)} Python files:\n")
    for file in files:
        print(file)