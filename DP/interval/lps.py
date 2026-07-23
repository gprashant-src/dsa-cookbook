def lpss(s):
    n = len(s)

    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    start, length = 0, 1

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] != s[j]:
                dp[i][j] = False
            elif j - i <= 2:
                dp[i][j] = True
            else:dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j] and length < l:
                length = l
                start = i

    return s[start:start+length]

