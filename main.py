from sympy import primerange
from collections import defaultdict
limit = 200

arr = list(primerange(limit))

f = lambda x, p: (x ** 3 - 3 * x + 4) % p

def find(p):
    A = 1
    for x in range(p):
        A = (A * f(x, p)) % p
        if A == 0:
            return 0, x
    else:
        return A, p

H = defaultdict(list)

for p in arr:
    a, b = find(p)
    H[b].append(p)

for k, v in sorted(H.items()):
    print(k ,"->", v)