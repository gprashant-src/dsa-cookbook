from collections import defaultdict

def f(n, arr):
    tree = defaultdict(list)
    
    for v, u in enumerate(arr, start=2):
        tree[u].append(v)

    stack = [1]
    order = []
    while stack:
        curr = stack.pop()
        order.append(curr)
        for v in tree[curr]:
            stack.append(v)

    H = [0] * (n + 1)
    for node in reversed(order):
        for v in tree[node]:
            H[node] += 1 + H[v]


n = int(input())
arr = list(map(int, input().split()))
print(f(n, arr))