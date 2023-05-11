from node import Node
from work_with_graph import make_graph, print_graph, make_adjacency_matrix, print_adjacency_matrix

from Bellman_Ford import bellman_ford
from Dijkstra import dijkstra


def johnson(adjacency_matrix: list):

    final_matrix = []
    for i in range(len(adjacency_matrix)):
        final_matrix.append(adjacency_matrix[i].copy())

    path_matrix = []
    for i in range(len(adjacency_matrix)):
        path_matrix.append([])
        for j in range(len(adjacency_matrix)):
            path_matrix[i].append(0)

    for i in range(len(adjacency_matrix)):
        adjacency_matrix[i].append('')

    graph_to_return = make_graph(adjacency_matrix, 0)

    helper = []
    for i in range(len(adjacency_matrix[0])):
        helper.append(0)

    adjacency_matrix.append(helper)

    nodes = bellman_ford(adjacency_matrix, len(adjacency_matrix)-1)

    for i in range(len(nodes)):
        for j in nodes[i].connections.keys():
            nodes[i].change_connection(j, nodes[i].connections[j] + nodes[i].weight - nodes[j.name].weight)

    name = nodes[len(nodes)-1].name
    for i in range(len(nodes)):
        nodes[i].delete_connection(name)
    nodes.pop(len(nodes)-1)

    for i in range(len(nodes)):
        nodes_copy = nodes.copy()
        graph = dijkstra(make_adjacency_matrix(nodes_copy), i)

        for j in range(len(graph)):
            final_matrix[i][j] = graph[j].weight
            path_matrix[i][j] = graph[j].path

    for i in range(len(final_matrix)):
        for j in range(len(final_matrix[0])):
            #if type(final_matrix[i][j]) != str:
            final_matrix[i][j] = final_matrix[i][j] - nodes[i].weight + nodes[j].weight

    return final_matrix, path_matrix, graph_to_return
