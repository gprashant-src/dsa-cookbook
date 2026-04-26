from collections import deque

# Graph BFS
def bfs(graph, start):
    q = deque([start])
    visited = set()

    while q:
        curr = q.popleft()
        # Process node
        for neigh in graph[curr]:
            if neigh not in visited:
                q.append(neigh)
                visited.add(neigh)
    
# Graph level BFS
def bfs(graph, start):
    q = deque([start])
    visited = set()

    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            # Process node
            for neigh in graph[curr]:
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)