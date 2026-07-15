import networkx as nx
from app.parser.repository_scanner import RepositoryScanner
from app.parser.ast_parser import ASTParser


class DependencyGraph:

    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.graph = nx.DiGraph()

    def build(self):
        scanner = RepositoryScanner(self.repo_path)
        files = scanner.get_python_files()

        for file in files:
            parser = ASTParser(str(file))
            info = parser.parse()

            file_name = str(file)
            self.graph.add_node(file_name)

            for module in info["imports"]:
                self.graph.add_edge(file_name, module)

        return self.graph


if __name__ == "__main__":

    graph = DependencyGraph(".")
    g = graph.build()

    print("\nDependency Graph\n")

    print("Nodes:\n")
    for node in g.nodes():
        print(node)

    print("\nEdges:\n")
    for edge in g.edges():
        print(edge)