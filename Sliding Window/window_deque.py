from collections import deque

nums = [1,3,-1,-3,5,3,6,7]
k = 3

d = deque()
res = []

for i in range(len(nums)):
    while d and nums[d[-1]] < nums[i]:
        d.pop()

    d.append(i)

    if d[0] == i - k:
        d.popleft()

    if i >= k - 1: res.append(nums[d[0]])

print(res)