from collections import defaultdict


class Graph:
    def __init__(self, directed = False):
        self.nodes = defaultdict(list)
        self.directed = directed

    def add_edge(self, v1, v2, weight = None):        
        self.nodes[v1].append([v2, weight] if weight else v2)

        if not self.directed:
            self.nodes[v2].append([v1, weight] if weight else v1)

    def __str__(self):
        message = ''

        for node in self.nodes:
            message += f'{node}\n'

        return message


def dfs(graph: Graph, origin, search):
    visited = defaultdict(bool)
    stack = [[origin]]

    while stack:
        path = stack.pop()

        actual = path[-1]

        if actual == search:
            return path

        visited[actual] = True

        for adjacent in graph.nodes[actual]:

            if not visited[adjacent]:
                new_path = list(path)
                new_path.append(adjacent)

                if adjacent == search:
                    return new_path

                stack.append(new_path)

    return []

