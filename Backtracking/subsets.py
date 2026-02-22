nums = [1, 2, 3, 4]
res = []

def f(start, path):
    res.append(path.copy())
    for end in range(start, len(nums)):
        if end > start and nums[end] == nums[end - 1]:
            continue

        path.append(nums[end])
        f(end + 1, path)
        path.pop()

f(0, [])
print(res)