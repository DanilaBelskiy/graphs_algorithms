from pyvis.network import Network

g = Network(notebook=True)

g.add_nodes([1, 2, 3],
            value=[10, 10, 10],
            title=['I am node 1', 'node 2 here', 'and im node 3'],
            x=[50, 100, 150],
            y=[100, 100, 100],
            label=['1', '2', '3'],
            color=['red', 'green', 'blue'])

g.add_edge(1, 2)
g.add_edge(3, 2)

g.toggle_physics(True)

g.show("basic.html")