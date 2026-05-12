def bellman(n, edges, start):
    INF = 10**18

    dist = [INF] * (n + 1)
    dist[start] = 0

    for _ in range(n - 1):
        flag = False

        for u, v, w in edges:
            if dist[u] == INF: continue

            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                flag = True
        
        if not flag:
            break
    
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    
    return dist
       