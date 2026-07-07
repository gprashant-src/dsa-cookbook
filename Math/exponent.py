a = 10000
b = 34
c = 30
MOD = 14

print(pow(a, b, MOD))

# Tower exponent
print(pow(a, pow(b, c, MOD - 1), MOD))