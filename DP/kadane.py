def kadane(nums):
    curr, MAX = 0, -float("inf")

    for num in nums:
        curr = max(num, curr + num)
        MAX = max(MAX, curr)
    
    return MAX