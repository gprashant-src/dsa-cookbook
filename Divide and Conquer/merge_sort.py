arr = [1, 4, 3, 2, 6, 10, 8]

def combine(left, right):
    res = []
    m, n = len(left), len(right)

    i, j = 0, 0
    while i < m and j < n:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    while i < m:
        res.append(left[i])
        i += 1
    
    while j < n:
        res.append(right[j])
        j += 1
    
    return res

def f(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = f(arr[:mid])
    right = f(arr[mid:])

    return combine(left, right)

print(f(arr))

