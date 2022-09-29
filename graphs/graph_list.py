from collections import defaultdict


class Graph:
    def __init__(self, directed = False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, v1, v2, weight = None):        
        self.graph[v1].append([v2, weight] if weight else v2)

        if not self.directed:
            self.grapf[v2].append([v1, weight] if weight else v1)

    def __str__(self):
        message = ''

        for node in self.graph:
            message += f'{node}\n'

        return message
