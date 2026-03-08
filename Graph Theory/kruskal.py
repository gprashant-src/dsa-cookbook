class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.n = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        self.parent[py] = px
        return True

n = 5
edges = [(0,1,1),(0,2,7),(1,2,5),(1,3,4),(3,4,2),(2,4,6),(1,4,3)]

cost = 0
tot_edges = 0
edges.sort(key=lambda x:x[2])

dsu = DSU(5)
for u, v, e in edges:
    if dsu.union(u, v):
        cost += e
        tot_edges += 1
    
    if tot_edges == n - 1:
        break

print(cost)
