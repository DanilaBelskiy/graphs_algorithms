from work_with_graph import inf


def floyd(adjacency_matrix: list):

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if type(adjacency_matrix[i][j]) == str:
                adjacency_matrix[i][j] = inf()

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            for k in range(len(adjacency_matrix)):
                if adjacency_matrix[i][k] + adjacency_matrix[k][j] < adjacency_matrix[i][j]:
                    adjacency_matrix[i][j] = adjacency_matrix[i][k] + adjacency_matrix[k][j]

    return adjacency_matrix
