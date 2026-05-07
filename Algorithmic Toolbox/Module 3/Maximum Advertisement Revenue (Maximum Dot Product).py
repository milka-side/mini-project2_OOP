def max_dot_product(prices, clicks):
    prices.sort()
    clicks.sort()
    return sum(p * c for p, c in zip(prices, clicks))

if __name__ == '__main__':
    import sys
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        prices = list(map(int, input_data[1:n+1]))
        clicks = list(map(int, input_data[n+1:]))
        print(max_dot_product(prices, clicks))
