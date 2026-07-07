A = [[1, 2, 3],
     [4, 1, 2],
     [1, 3, 4]]

class prefix2d:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.P = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.P[i + 1][j + 1] = grid[i][j] + self.P[i + 1][j] + self.P[i][j + 1] - self.P[i][j]

    def query(self, x1, y1, x2, y2):    
        return self.P[x2 + 1][y2 + 1] - self.P[x1][y2 + 1] - self.P[x2 + 1][y1] + self.P[x1][y1]
    

pr = prefix2d(A)
print(pr.query(0, 0, 1, 1))