import math

def solve(n, m, arr, idx):
    V = len(set(idx))
    arr.sort(reverse=True)
    return sum(arr[V:])
    

t = int(input())

while t:
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = list(map(int, input().split()))
    print(solve(n, m, arr, idx))
    t -= 1