from node import Node
from work_with_graph import make_graph, print_graph

from Bellman_Ford import bellman_ford
from Dijkstra import dijkstra


def johnson(adjacency_matrix: list):

    for i in range(len(adjacency_matrix)):
        adjacency_matrix[i].append('')

    helper = []
    for i in range(len(adjacency_matrix[0])):
        helper.append(0)

    adjacency_matrix.append(helper)

    nodes = bellman_ford(adjacency_matrix, len(adjacency_matrix)-1)

    for i in range(len(nodes)):
        for j in nodes[i].connections.keys():
            nodes[i].change_connection(j, nodes[i].connections[j] + nodes[i].weight - nodes[j.name].weight)

    print_graph(nodes)

    name = nodes[len(nodes)-1].name
    for i in range(len(nodes)):
        nodes[i].delete_connection(name)
    nodes.pop(name)

    final_matrix = adjacency_matrix

    for i in range(len(nodes)):
        graph_copy = nodes

        dijkstra(nodes)

    return nodes
