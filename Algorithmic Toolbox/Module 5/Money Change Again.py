def change(money):
    min_coins = [0] * (money + 1)
    coins = [1, 3, 4]
    for m in range(1, money + 1):
        min_coins[m] = float('inf')
        for coin in coins:
            if m >= coin:
                num_coins = min_coins[m - coin] + 1
                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins
    return min_coins[money]

if __name__ == '__main__':
    import sys
    m = int(sys.stdin.read())
    print(change(m))
