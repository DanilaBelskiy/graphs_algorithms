from work_with_graph import inf


def floyd(adjacency_matrix: list):

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if type(adjacency_matrix[i][j]) == str:
                adjacency_matrix[i][j] = inf()

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            for k in range(len(adjacency_matrix)):
                if adjacency_matrix[j][i] + adjacency_matrix[i][k] < adjacency_matrix[j][k]:
                    adjacency_matrix[j][k] = adjacency_matrix[j][i] + adjacency_matrix[i][k]

    return adjacency_matrix
