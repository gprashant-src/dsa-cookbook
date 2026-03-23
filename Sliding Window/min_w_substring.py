from collections import defaultdict, Counter
s = "ADOBECODEBANC"
t = "ABC"

H = Counter(t)
T = defaultdict(int)

ans, length = "", float("inf")

need= len(H)
done = 0

l = 0
for r in range(len(s)):
    T[s[r]] += 1
    if s[r] in H and H[s[r]] == T[s[r]]:
        done += 1
    
    while done == need:
        if (r - l + 1) < length:
            length = r - l + 1
            ans = s[l:r + 1]
        
        T[s[l]] -= 1
        if s[l] in H and T[s[l]] < H[s[l]]:
            done -= 1
        
        l += 1

print(ans)