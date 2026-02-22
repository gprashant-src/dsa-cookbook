k = 4
box = [0] * k
nums = [1, 3, 4, 5, 6]
target = 7

def f(index):
    if index == len(nums):
        return True
    
    for i in range(k):
        if box[i] + nums[index] > target:
            continue

        box[i] += nums[index]
        if f(index + 1): return True
        box[i] += nums[index]

        if box[i] == 0:
            break
    
    return False

print(f(0))