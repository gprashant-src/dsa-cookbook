from collections import defaultdict, deque

def topo_kahn(n, edges):
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    for u, v in edges:
        graph[u].append(v)
        # graph[v].append(u)
        indegree[v] += 1
    
    topo = []
    q = deque([i for i in range(1, n + 1) if indegree[i] == 0])

    while q:
        node = q.popleft()

        topo.append(node)

        for v in graph[node]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
        
    if len(topo) < n: return "IMPOSSIBLE"
    return " ".join(map(str, topo))    