import heapq
freq = [120, 37, 42, 42, 32, 2, 7, 24]
# print(sum(freq))

heapq.heapify(freq)

ans = 0
while len(freq) > 1:
    a = heapq.heappop(freq)
    b = heapq.heappop(freq)
    # print(a, b, "=", a + b)
    # ans += (a + b)
    heapq.heappush(freq, a + b)

print(ans)