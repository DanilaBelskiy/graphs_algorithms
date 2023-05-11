from pyvis.network import Network
from node import Node


def visual_graph(graph: list, start_node: int = 0, end_node: int = 0, name: str = 'basic.html'):

    net = Network(notebook=True, directed=True)

    for i in range(len(graph)):
        net.add_node(graph[i].name, size=20, value=graph[i].weight, label=str(graph[i].name),
                     title=str(graph[i].weight) + " " + str(graph[i].path), x=50, y=100)

    net.nodes[start_node]['color'] = 'red'
    net.nodes[end_node]['color'] = 'green'

    for i in range(1, len(graph[end_node].path)-1):
        net.nodes[graph[end_node].path[i]]['color'] = 'yellow'

    for i in range(len(graph)):
        for j in graph[i].connections.keys():
            net.add_edge(graph[i].name, j.name, weight=graph[i].connections[j], label=str(graph[i].connections[j]))

    net.toggle_physics(True)
    net.show(name)


def visual_matrix_johnson(distances_matrix: list, path_matrix: list, graph: list, start_node: int = 0, end_node: int = 0,
                  name: str = 'basic.html'):

    net = Network(notebook=True, directed=True)

    for i in range(len(graph)):
        net.add_node(graph[i].name, size=20, value=distances_matrix[start_node][i], label=str(graph[i].name),
                     title=str(distances_matrix[start_node][i]) + " " + str(path_matrix[start_node][i]), x=50, y=100)

    net.nodes[start_node]['color'] = 'red'
    net.nodes[end_node]['color'] = 'green'

    for i in range(1, len(path_matrix[start_node][end_node])-1):
        net.nodes[path_matrix[start_node][end_node][i]]['color'] = 'yellow'

    for i in range(len(graph)):
        for j in graph[i].connections.keys():
            net.add_edge(graph[i].name, j.name, weight=graph[i].connections[j], label=str(graph[i].connections[j]))

    net.toggle_physics(True)
    net.show(name)


def visual_matrix_floyd(distances_matrix: list, path_matrix: list, graph: list, start_node: int = 0, end_node: int = 0,
                        name: str = 'basic.html'):

    net = Network(notebook=True, directed=True)

    for i in range(len(graph)):
        net.add_node(graph[i].name, size=20, value=distances_matrix[start_node][i], label=str(graph[i].name),
                     title=str(distances_matrix[start_node][i]), x=50, y=100)

    net.nodes[start_node]['color'] = 'red'
    net.nodes[end_node]['color'] = 'green'

    u = start_node
    path = [start_node]
    while u != end_node:
        u = path_matrix[u][end_node]
        path.append(u)

    net.nodes[end_node]['title'] += str(path)

    for i in range(1, len(path)-1):
        net.nodes[path[i]]['color'] = 'yellow'

    for i in range(len(graph)):
        for j in graph[i].connections.keys():
            net.add_edge(graph[i].name, j.name, weight=graph[i].connections[j], label=str(graph[i].connections[j]))

    net.toggle_physics(True)
    net.show(name)
