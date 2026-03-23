from collections import defaultdict

s = "abcabcbb"
H = defaultdict(int)

l = 0
ans = 0
for r in range(len(s)):
    H[s[r]] += 1
    while H[s[r]] > 1:
        H[s[l]] -= 1
        l += 1
    ans = max(ans, r - l + 1)

print(ans)
