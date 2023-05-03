from Dijkstra import dijkstra
from Bellman_Ford import bellman_ford
from Johnson import johnson

from adjacency_matrices import adjacency_matrix1, adjacency_matrix2, adjacency_matrix3,\
    adjacency_matrix4, adjacency_matrix5

from work_with_graph import print_graph

print_graph(johnson(adjacency_matrix4))
