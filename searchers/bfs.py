from graphs.graph_list import Graph, defaultdict


def bfs(graph: Graph, origin, search):
    visited = defaultdict(bool)
    queue = [[origin]]

    while queue:
        path = queue.pop(0)

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

                queue.append(new_path)

    return []
