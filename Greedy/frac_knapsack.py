items = [(10, 50), (20, 120), (30, 150), (40, 210), (50, 240)]

items.sort(key=lambda x:x[1]/x[0], reverse=True)

S = 0
W = 50

for wi, vi in items:
    if wi <= W:
        S += vi
        W -= wi
    else:
        S += (vi * W / wi)
        break

print(S)

