from Dijkstra import dijkstra
from Bellman_Ford import bellman_ford
from Johnson import johnson
from Floyd import floyd

from adjacency_matrices import adjacency_matrix1, adjacency_matrix2, adjacency_matrix3,\
    adjacency_matrix4, adjacency_matrix5, adjacency_matrix6, adjacency_matrix7

from work_with_graph import print_graph, print_adjacency_matrix
from visual import visual_graph, visual_matrix_johnson, visual_matrix_floyd


algorithms = {0: 'Dijkstra', 1: 'Bellman_Ford', 2: 'Johnson', 3: 'Floyd'}
algorithm = 3
adjacency_matrix = adjacency_matrix4
start_node = 0
end_node = 8

if algorithm == 0:

    graph = dijkstra(adjacency_matrix, start_node)
    visual_graph(graph, start_node, end_node, "dijkstra.html")

elif algorithm == 1:

    graph = bellman_ford(adjacency_matrix, start_node)
    visual_graph(graph, start_node, end_node, "bellman_ford.html")

elif algorithm == 2:

    distances_matrix, path_matrix, graph = johnson(adjacency_matrix)
    visual_matrix_johnson(distances_matrix, path_matrix, graph, start_node, end_node, "johnson.html")

elif algorithm == 3:

    distances_matrix, path_matrix, graph = floyd(adjacency_matrix)
    visual_matrix_floyd(distances_matrix, path_matrix, graph, start_node, end_node, "floyd.html")
