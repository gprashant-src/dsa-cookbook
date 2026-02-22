nums = [4, 3, 5, 10, 1, 2, 3]
res = []

def f(start, path):
    if len(path) > 1:
        res.append(path.copy())
    
    visited = set()

    for i in range(start, len(nums)):
        if nums[i] in visited:
            continue

        if not path or nums[i] >= path[-1]:
            visited.add(nums[i])
            path.append(nums[i])
            f(i + 1, path)
            path.pop()

f(0, [])
print(res)