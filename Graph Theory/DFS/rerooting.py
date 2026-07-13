from collections import defaultdict

graph = defaultdict(list)
n = 6

edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
    

size = [1] * n
ans = [0] * n




def dfs1(node, par, depth):
    ans[0] += depth

    for neigh in graph[node]:
        if neigh != par:
            dfs1(neigh, node, depth + 1)
            size[node] += size[neigh]
    
def dfs2(node, par):
    for neigh in graph[node]:
        if neigh != par:
            ans[neigh] = ans[node] - 2 * size[neigh] + n
            dfs2(neigh, node)

dfs1(0, -1, 0)
dfs2(0, -1)

print(ans)