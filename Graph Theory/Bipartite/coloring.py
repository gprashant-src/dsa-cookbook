from collections import defaultdict, deque

graph = defaultdict(list)

def coloring(n, graph):
    color = [0] * (n + 1)

    def bfs(start):
        q = deque([start])
        color[start] = 1

        while q:
            curr = q.popleft()

            for neigh in graph[curr]:
                if color[neigh] == 0:
                    color[neigh] = 3 - color[curr]
                    q.append(neigh)

                elif color[neigh] == color[curr]:
                    return False
        
        return True
    
    ans = True
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                ans = False
                break
    
    if not ans:
        return False
    return color[1:]