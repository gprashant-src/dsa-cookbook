arr = [1, 4, 3, 2, 6, 10, 8]

P = [0] * (len(arr) + 1)

for i in range(len(arr)):
    P[i + 1] = P[i] + arr[i]

l, r = 2, 5
print(P)
print("Range sum=",  P[r + 1] - P[l])