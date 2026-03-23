nums = [10,5,2,6]
k = 100

if k <= 1:
    print(0)
    exit(0)
l = 0
P = 1
ans = 0
for r in range(len(nums)):
    P *= nums[r]

    while P >= k:
        P //= nums[l]
        l += 1
    
    ans += (r - l + 1)

print(ans)