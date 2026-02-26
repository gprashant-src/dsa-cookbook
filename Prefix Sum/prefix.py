arr = [1, 4, 3, 2, 6, 10, 8]

def prefix1d(arr):
    P = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        P[i + 1] = P[i] + arr[i]

    return P

def range1d(l, r, P):
    return P[r + 1] - P[l]
l, r = 2, 5

P = prefix1d(arr)
# print(P)
print("Range sum=",range1d(l, r, P))