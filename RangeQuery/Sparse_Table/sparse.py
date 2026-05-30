from math import log2, floor

class sparse1d:
    def __init__(self, arr):
        self.k = floor(log2(len(arr)))
        self.n = len(arr)
        self.table = [[0] * (self.k + 1) for _ in range(self.n)]

        for i in range(self.n):
            self.table[i][0] = arr[i]

        for j in range(1, self.k + 1):
            for i in range(self.n - (1 << j) + 1):
                self.table[i][j] = min(self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1])
    
    def query(self, left, right):
        size = right - left + 1

        k = floor(log2(size))
        return min(self.table[left][k], self.table[right - (1 << k) + 1][k])

arr = [7, 2, 5, 1, 9, 3]
sp = sparse1d(arr)

for row in sp.table:
    print(*row)

l, r = 1, 5
print(sp.query(l, r))