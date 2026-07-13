def legendre(n, p):
    k = 0
    i = p
    while i <= n:
        k += n // i
        i *= p
    return k