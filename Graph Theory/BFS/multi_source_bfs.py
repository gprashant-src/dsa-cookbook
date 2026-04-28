from collections import deque

def multi_source_bfs(grid):
    m, n = len(grid), len(grid[0])

    res = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1: # or any condition to find the source
                res[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and res[nx][ny] == -1:
                res[nx][ny] = res[x][y] + 1
                q.append((nx, ny))
    
    return res