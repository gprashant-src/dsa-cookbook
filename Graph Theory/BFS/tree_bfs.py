from collections import deque

# Tree BFS
def tree_bfs(root):
    q = deque([root])

    while q:
        curr = q.popleft()
        # Process node
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    
# Tree level BFS
def bfs(root):
    q = deque([root])

    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            # Process node
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)