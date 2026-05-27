A = [[1, 2, 3],
     [4, 1, 2],
     [1, 3, 4]]

def prefix2d(A):
    m, n = len(A), len(A[0])
    P = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            P[i + 1][j + 1] = A[i][j] + P[i + 1][j] + P[i][j + 1] - P[i][j]

    return P

def range2d(x1, y1, x2, y2, P):
    return P[x2 + 1][y2 + 1] - P[x1][y2 + 1] - P[x2 + 1][y1] + P[x1][y1]

P = prefix2d(A)
print(range2d(0, 0, 1, 1, P))