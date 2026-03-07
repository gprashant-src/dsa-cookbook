jobs = []
n = int(input("Enter the no.of jobs:"))


for _ in range(n):
    d, p = map(int, input().split())
    jobs.append((d, p))

max_d = max(d for d, _ in jobs)

slots = [False] * (max_d + 1)

jobs.sort(key=lambda x:x[1], reverse=True)

S = 0
for d, p in jobs:
    for t in range(d, 0, -1):
        if not slots[t]:
            slots[t] = True
            S += p
            break

print(S)

