n1 = 788
n2 = 123

def f(x, y):
    if x < 10 and y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    D = 10 ** m
    a, b = divmod(x, D)
    c, d = divmod(y, D)

    ac = f(a, c)
    bd = f(b, d)
    ad_bc = (a + b) * (c + d) - ac - bd

    return ac * (10 ** (2*m)) + ad_bc * (10 ** m) + bd

print(f(n1, n2))
