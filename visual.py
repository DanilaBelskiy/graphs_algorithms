from pyvis.network import Network
from node import Node


def visual_graph(graph: list, name: str = 'basic.html'):

    net = Network(notebook=True)

    for i in range(len(graph)):
        net.add_node(graph[i].name, size=20, value=graph[i].weight, label=str(graph[i].name),
                     title=str(graph[i].weight), x=50, y=100)

    for i in range(len(graph)):
        for j in graph[i].connections.keys():
            net.add_edge(graph[i].name, j.name, weight=graph[i].connections[j], label=str(graph[i].connections[j]))

    net.toggle_physics(True)
    net.show(name)
