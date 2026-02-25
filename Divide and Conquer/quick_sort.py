arr = [1, 4, 3, 2, 6, 10, 8]

def part(low, high):
    # global arr
    ans = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= ans:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
    
def qs(low, high):
    if low < high:
        pi = part(low, high)
        qs(low, pi - 1)
        qs(pi + 1, high)

qs(0, len(arr) - 1)
print(arr)