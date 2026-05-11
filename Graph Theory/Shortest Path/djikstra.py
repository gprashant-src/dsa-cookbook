import heapq

def dijkstra(n, graph, start):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0

    h = [(0, start)]

    while h:
        d, u = heapq.heappop(h)

        if d > dist[u]: continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(h, (nd, v))
    
    print(dist)