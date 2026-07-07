MOD = 10**9 + 7

# divisor count

def count(n):
    i = 2
    P = 1
    while i * i <= n:
        if n % i == 0:
            c = 0
            while n % i == 0:
                n //= i
                c += 1
            P = P * (c + 1)
        i += 1
    if n > 1:
        P *= 2
    return P

n = 18
print(count(n))


# Sum of divisors

def div_count(n):
    def GP(p, a):
        num = pow(p, a + 1, M) - 1
        den = pow(p - 1, MOD - 2, MOD)
        return ((num % MOD) * (den % MOD)) % MOD

    i = 2
    P = 1
    while i * i <= n:
        if n % i == 0:
            c = 0
            while n % i == 0:
                n //= i
                c += 1
            ax = GP(i, c)
            P = (P * ax) % MOD
        i += 1
    if n > 1:
        P = (P * (n + 1)) % MOD
    return P