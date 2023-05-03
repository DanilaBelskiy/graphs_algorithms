from node import Node
from work_with_graph import make_graph, change_weight_of_node, print_graph


def dijkstra(adjacency_matrix: list, start_node: int = 0):
    def check_node(node: Node, nodes_arr):
        for i in node.connections.keys():
            #if not nodes_arr[i.name].is_closed():
                change_weight_of_node(node, nodes[i.name])

        node.close()

        node.sort_connections()

        #print_graph(nodes)

        for i in node.connections.keys():
            if not nodes_arr[i.name].is_closed():
                check_node(nodes[i.name], nodes)

    nodes = make_graph(adjacency_matrix, start_node)

    check_node(nodes[start_node], nodes)

    return nodes
