from collections import defaultdict

def cycle_find(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        # graph[v].append(u)  # Uncomment this for undirected graphs
    
    visited = [0] * (n + 1)  
    parent = [-1] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start] == 0:
            stack = [(start, -1, 0)] 
            while stack:
                node, par, state = stack.pop()
                
                if state == 1: 
                    visited[node] = 2
                    continue
                
                # entering node
                if visited[node] == 1:  
                    continue
                    
                visited[node] = 1
                parent[node] = par
                
 
                stack.append((node, par, 1))
                
 
                for neigh in graph[node]:
                    # if neigh == par:          # Uncomment this block for undirected graphs
                    #     continue
                    
                    if visited[neigh] == 0:  
                        stack.append((neigh, node, 0))
                    elif visited[neigh] == 1:  
 
                        cycle = [neigh]
                        curr = node
                        while curr != neigh:
                            cycle.append(curr)
                            curr = parent[curr]
                        cycle.append(neigh)
                        return f"{len(cycle)}\n{' '.join(map(str, cycle[::-1]))}"
    
    return "IMPOSSIBLE"