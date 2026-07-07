# GCD based sieve

def max_gcd(arr):
    M = max(arr)
    count = [0] * (M + 1)

    for N in arr:
        count[N] += 1
    
    for i in range(M, 0, -1):
        c = 0
        for j in range(i, M + 1, i):
            c += count[j]
            if c >= 2:return i


# Divisor sum sieve

def div_count(n):
    count = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            count[j] += i
    return count
