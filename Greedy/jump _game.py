nums = [2, 3, 1, 1, 4]
M = 0
for i in range(len(nums)):
    if i > M:
        print(False)
        exit()
    M = max(M, i + nums[i])
print(True)