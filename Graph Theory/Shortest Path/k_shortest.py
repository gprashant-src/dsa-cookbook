import heapq

def k_shortest(n, graph, k):
    start = 1
    dist = [float("inf")] * (n + 1)
    dist[start] = 0

    count = [0] * (n + 1)
 
    h = [(0, start)]
    val = []
    while h:
        d, u = heapq.heappop(h)


        if count[u] >= k: continue
        count[u] += 1

        if u == n:
            val.append(d)
 
        # if d > dist[u]: continue
        
 
        for v, w in graph[u]:
            nd = d + w
            if count[v] < k:
            # if nd < dist[v]:
            #     dist[v] = nd
                heapq.heappush(h, (nd, v))
    
    return " ".join(map(str, val))
