from node import Node
from work_with_graph import make_graph, change_weight_of_node, print_graph


def dijkstra(adjacency_matrix: list, start_node: int = 0):
    def is_node_in(node: Node, nodes_arr: list):
        for i in range(len(nodes_arr)):
            if node.name == nodes_arr[i].name:
                return True
        return False

    def check_nodes(node: Node, nodes_arr, queue: list):

        queue.append(node)

        print("Queue: ")
        for j in range(len(queue)):
            print(queue[j].name, end=" ")
        print()

        while len(queue) > 0:

            current_node = queue.pop(0)

            for i in current_node.connections.keys():
                #if not nodes_arr[i.name].is_closed():
                    change_weight_of_node(current_node, nodes_arr[i.name])

            current_node.close()
            current_node.sort_connections()

            print("Queue: ")
            for j in range(len(queue)):
                print(queue[j].name, end=" ")
            print()

            print_graph(nodes_arr)

            for i in current_node.connections.keys():
                if not (nodes_arr[i.name].is_closed()): #and not (is_node_in(nodes_arr[i.name], queue)):
                    print(i.name, len(nodes_arr), len(queue))
                    queue.append(nodes_arr[i.name])

            print("Queue: ")
            for j in range(len(queue)):
                print(queue[j].name, end=" ")
            print()

    queue = []

    nodes = make_graph(adjacency_matrix, start_node)

    check_nodes(nodes[start_node], nodes, queue)

    return nodes
