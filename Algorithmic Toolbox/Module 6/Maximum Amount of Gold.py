def maximum_gold(capacity, weights):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                val = dp[i-1][w - weights[i-1]] + weights[i-1]
                if val > dp[i][w]:
                    dp[i][w] = val
    return dp[n][capacity]

if __name__ == '__main__':
    import sys
    data = list(map(int, sys.stdin.read().split()))
    capacity, n, weights = data[0], data[1], data[2:]
    print(maximum_gold(capacity, weights))
