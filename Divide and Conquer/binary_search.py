arr = [1, 4, 3, 2, 6, 10, 8]
arr.sort()
target = 6

def f(low, high):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        return f(low, mid - 1)
    else:
        return f(mid + 1, high)
    

def fi(low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

print(fi(0, len(arr) - 1))