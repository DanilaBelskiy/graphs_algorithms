from work_with_graph import inf, make_graph


def floyd(adjacency_matrix: list):

    path_arr = []
    graph_to_return = make_graph(adjacency_matrix)

    for i in range(len(adjacency_matrix)):
        path_arr.append([])
        for j in range(len(adjacency_matrix)):
            path_arr[i].append(j)

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if type(adjacency_matrix[i][j]) == str:
                adjacency_matrix[i][j] = inf()

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            for k in range(len(adjacency_matrix)):
                if adjacency_matrix[j][i] + adjacency_matrix[i][k] < adjacency_matrix[j][k]:
                    adjacency_matrix[j][k] = adjacency_matrix[j][i] + adjacency_matrix[i][k]
                    path_arr[j][k] = path_arr[j][i]

    for i in range(len(path_arr)):
        for j in range(len(path_arr[i])):
            print(path_arr[i][j], end=' ')
        print()

    return adjacency_matrix, path_arr, graph_to_return
