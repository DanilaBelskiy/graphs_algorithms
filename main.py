from Dijkstra import dijkstra
from Bellman_Ford import bellman_ford
from Johnson import johnson
from Floyd import floyd

from adjacency_matrices import adjacency_matrix1, adjacency_matrix2, adjacency_matrix3,\
    adjacency_matrix4, adjacency_matrix5, adjacency_matrix6, adjacency_matrix7

from work_with_graph import print_graph, print_adjacency_matrix
from visual import visual_graph, visual_matrix_johnson, visual_matrix_floyd

#print_adjacency_matrix(johnson(adjacency_matrix4))

'''distances_matrix, path_matrix, graph = johnson(adjacency_matrix4)
visual_matrix_johnson(distances_matrix, path_matrix, graph, 0, 5, "4.html")'''

distances_matrix, path_matrix, graph = floyd(adjacency_matrix4)
visual_matrix_floyd(distances_matrix, path_matrix, graph, 0, 8, "4.html")
