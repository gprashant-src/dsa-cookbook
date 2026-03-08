from collections import defaultdict
import heapq

graph = defaultdict(list)
n = 5
edges = [(0,1,1),(0,2,7),(1,2,5),(1,3,4),(3,4,2),(2,4,6),(1,4,3)]

MST = set()
for u, v, e in edges:
    heapq.heappush(graph[v], (e, u))
    heapq.heappush(graph[u], (e, v))

start = 0
MST.add(start)
cost = 0

while len(MST) < n:
    temp = list(MST)
    for u in temp:
        e,v = heapq.heappop(graph[u])
        if v not in MST:
            MST.add(v)
            cost += e
            continue
        heapq.heappush(graph[u], (e, v))

print(cost)



    