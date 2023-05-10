from node import Node
from work_with_graph import make_graph, change_weight_of_node, print_graph


def bellman_ford(adjacency_matrix: list, start_node: int = 0):
    nodes = make_graph(adjacency_matrix, start_node)

    print_graph(nodes)

    nodes[start_node].set_path([nodes[start_node].name])

    for i in range(len(nodes) - 1):
        for j in range(len(nodes)):
            for k in nodes[j].connections.keys():
                if nodes[j].weight + nodes[j].connections[k] < k.weight:
                    change_weight_of_node(nodes[j], nodes[k.name])
                    nodes[k.name].set_path(nodes[j].path + [nodes[k.name].name])

    is_infinite_loop = False

    for i in range(len(nodes) - 1):
        for j in range(len(nodes)):
            for k in nodes[j].connections.keys():
                if nodes[j].connections[nodes[k.name]] + nodes[j].weight < nodes[k.name].weight:
                    is_infinite_loop = True

    if is_infinite_loop:
        print("Infinite loop")

    return nodes
