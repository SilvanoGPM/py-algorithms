class Graph:
    def __init__(self, nodes, directed = False):
        self.graph = [[0] * nodes for _ in range(nodes)]
        self.nodes = nodes
        self.directed = directed

    def add_edge(self, v1, v2, weight = 1):
        self.graph[v1 - 1][v2 - 1] += weight

        if not self.directed:
            self.graph[v2 - 1][v1 - 1] += weight

    def __str__(self):
        message = ''

        for row in self.graph:
            message += str(row)

        return message
