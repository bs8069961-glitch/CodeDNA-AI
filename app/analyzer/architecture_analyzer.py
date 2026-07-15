from app.parser.repository_scanner import RepositoryScanner


class ArchitectureAnalyzer:

    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def analyze(self):
        scanner = RepositoryScanner(self.repo_path)
        files = scanner.get_python_files()

        architecture = {
            "api": [],
            "parser": [],
            "services": [],
            "utils": [],
            "vectorstore": [],
            "others": []
        }

        for file in files:

            path = str(file).lower()

            if "parser" in path:
                architecture["parser"].append(path)

            elif "service" in path or "services" in path:
                architecture["services"].append(path)

            elif "utils" in path:
                architecture["utils"].append(path)

            elif "vectorstore" in path:
                architecture["vectorstore"].append(path)

            elif "main.py" in path:
                architecture["api"].append(path)

            else:
                architecture["others"].append(path)

        return architecture


if __name__ == "__main__":

    analyzer = ArchitectureAnalyzer(".")
    result = analyzer.analyze()

    for category, files in result.items():

        print("\n", category.upper())

        for file in files:
            print("  ", file)