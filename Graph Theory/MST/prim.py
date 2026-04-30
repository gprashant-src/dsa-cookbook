from collections import defaultdict
import heapq

graph = defaultdict(list)
n = 5
edges = [(0,1,1),(0,2,7),(1,2,5),(1,3,4),(3,4,2),(2,4,6),(1,4,3)]

MST = set()

for u, v, e in edges:
    graph[u].append((e, v))
    graph[v].append((e, u))

MST = set()
cost = 0
heap = [(0, 0)]

while len(MST) < n:
    w, u = heapq.heappop(heap)
    if u in MST:
        continue

    MST.add(u)
    cost += w

    for edge in graph[u]:
        heapq.heappush(heap, edge)

print(cost)


    