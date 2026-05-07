def lcs2(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

if __name__ == '__main__':
    import sys
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:n+1]
    m = data[n+1]
    b = data[n+2:]
    print(lcs2(a, b))
