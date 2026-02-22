nums = [1, 2, 2, 4]
res = []
nums.sort()

visited = [False] * len(nums)

def f(path):
    if len(path) == len(nums):
        res.append(path.copy())
        return
    
    for end in range(len(nums)):
        if visited[end]:
            continue

        if end > 0 and nums[end] == nums[end - 1] and not visited[end - 1]:
            continue
        
        visited[end] = True
        path.append(nums[end])
        f(path)
        path.pop()
        visited[end] = False

f([])
print(res)