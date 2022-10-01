from graphs.graph_list import Graph, defaultdict

INFINITY = -1

def dijkstra(graph: Graph, origin):
    path_costs = defaultdict(lambda: {'from': 0, 'cost': INFINITY})
    path_costs[origin] = {'from': origin, 'cost': 0}

    heap = [[0, origin]]

    while heap:
        cost, node = heap.pop(0)

        for adjacent, weight in graph.graph[node]:
            adjacent_cost = path_costs[adjacent]['cost']
            
            if adjacent_cost == INFINITY or adjacent_cost > cost + weight:
                new_cost = cost + weight

                path_costs[adjacent] = {'from': node, 'cost': new_cost}
                heap.append([new_cost, adjacent])

                heap.sort()

    return path_costs