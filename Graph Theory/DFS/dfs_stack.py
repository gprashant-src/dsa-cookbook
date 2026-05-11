def dfs_stack(graph, start):
    visited = set()
    stack = [(start, -1)]

    while stack:
        u, par = stack.pop()

        if u not in visited:
            visited.add(u)
            for v in graph[u]:
                if v in visited:
                    if v != par: return True
                else:
                    stack.append((v, u))
    
    return False


sample_graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1],
    3: [0, 4],
    4: [3]
}

print(dfs_stack(sample_graph, 3))