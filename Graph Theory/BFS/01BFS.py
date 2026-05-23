from collections import defaultdict, deque

def zero_1_bfs(n, start):

    graph = defaultdict(int)
    INF = float('inf')

    dist = [INF] * n
    dist[start] = 0

    dq = deque([start])

    while dq:
        u = dq.popleft()

        for v, wt in graph[u]:
            new_dist = dist[u] + wt

            if new_dist < dist[v]:

                dist[v] = new_dist
                if wt == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    return dist