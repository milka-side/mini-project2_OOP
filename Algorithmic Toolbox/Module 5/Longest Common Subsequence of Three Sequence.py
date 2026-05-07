def lcs3(a, b, c):
    n, m, l = len(a), len(b), len(c)
    dp = [[[0]*(l+1) for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i-1] == b[j-1] == c[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1],
                                     dp[i-1][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1])
    return dp[n][m][l]

if __name__ == '__main__':
    import sys
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    n = data[idx]; idx += 1
    a = data[idx:idx+n]; idx += n
    m = data[idx]; idx += 1
    b = data[idx:idx+m]; idx += m
    q = data[idx]; idx += 1
    c = data[idx:idx+q]
    print(lcs3(a, b, c))
