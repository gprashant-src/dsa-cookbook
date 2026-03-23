nums = [1,12,-5,-6,50,3]
k = 4

Ws = sum(nums[:k])
M = Ws / k

for i in range(k, len(nums)):
    Ws = Ws + nums[i] - nums[i - k]
    M = max(M, Ws / k)

print(M)