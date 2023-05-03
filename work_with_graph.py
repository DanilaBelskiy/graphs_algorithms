from node import Node


def make_graph(edges: list, start_node: int) -> list:

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
    for i in range(len(graph)):
        pass


def change_weight_of_node(node_from: Node, node_to: Node):
    if node_from.connections[node_to] + node_from.weight < node_to.weight:
        node_to.weight = node_from.connections[node_to] + node_from.weight


def print_graph(nodes):
    for i in range(len(nodes)):
        nodes[i].print_node()
    print("--------------------------------------------------")
