import ast
from pathlib import Path


class ASTParser:
    """
    Parses a Python file and extracts:
    - Classes
    - Functions
    - Imports
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def parse(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source)

        result = {
            "classes": [],
            "functions": [],
            "imports": []
        }

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                result["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):
                result["functions"].append(node.name)

            elif isinstance(node, ast.Import):
                for alias in node.names:
                    result["imports"].append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                module = node.module if node.module else ""
                result["imports"].append(module)

        return result


if __name__ == "__main__":

    parser = ASTParser("app/main.py")

    info = parser.parse()

    print("\nAnalysis Result\n")

    print(info)