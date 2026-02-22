nums = [1, 2, 3, 4]
res = []
target = 5

def f(start, path, total):
    if total == target:
        res.append(path.copy())
        return
    
    if total > target:
        return
    
    for end in range(start, len(nums)):
        path.append(nums[end])
        f(end, path, total + nums[end])
        path.pop()
    
f(0, [], 0)
print(res)