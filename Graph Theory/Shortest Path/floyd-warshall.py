def floyd_warshall(n, graph):
    dist = [[float("inf")] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0
        for j, w in graph[i]:
            dist[i][j] = w

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    

