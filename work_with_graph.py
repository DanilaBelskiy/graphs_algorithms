from node import Node
import numpy


def make_graph(edges: list, start_node: int = 0) -> list:

    def inf():
        return float('inf')

    nodes = []

    for i in range(0, len(edges)):
        nodes.append(Node(i, inf()))
    nodes[start_node].weight = 0

    for i in range(len(edges)):
        for j in range(len(edges[0])):
            if i != j:
                if type(edges[i][j]) == int:
                    nodes[i].add_connection(nodes[j], edges[i][j])

    return nodes


def make_adjacency_matrix(graph: list):

    adjacency_matrix = []
    for i in range(len(graph)):
        adjacency_matrix.append([])
        for j in range(len(graph)):
            adjacency_matrix[i].append('')

    for i in range(len(graph)):
        for j in graph[i].connections.keys():
            adjacency_matrix[i][j.name] = int(graph[i].connections[j])

    return adjacency_matrix


def change_weight_of_node(node_from: Node, node_to: Node):
    if node_from.connections[node_to] + node_from.weight < node_to.weight:
        node_to.weight = node_from.connections[node_to] + node_from.weight


def inf():
    return float("inf")


def print_graph(nodes):
    for i in range(len(nodes)):
        nodes[i].print_node()
    print("--------------------------------------------------")


def print_adjacency_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()
