nums = [1, 2, 3, 4]
res = []
k = 2
visited = [False] * len(nums)

def f(path):
    if len(path) == k:
        res.append(path.copy())
        return
    
    for end in range(len(nums)):
        if not visited[end]:
            visited[end] = True
            path.append(nums[end])
            f(path)
            path.pop()
            visited[end] = False

f([])
print(res)