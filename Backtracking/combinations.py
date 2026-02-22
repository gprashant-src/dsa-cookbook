nums = [1, 2, 3, 4]
res = []
k = 2

def f(start, path):
    if len(path) == k:
        res.append(path.copy())
        return
    
    for end in range(start, len(nums)):
        path.append(nums[end])
        f(end + 1, path)
        path.pop()
    
f(0, [])
print(res)