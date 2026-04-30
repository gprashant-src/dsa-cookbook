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
