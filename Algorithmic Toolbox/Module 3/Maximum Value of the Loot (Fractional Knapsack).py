from sys import stdin


def optimal_value(capacity, weights, values):
    res = 0.
    items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)
    for v, w in items:
        if capacity == 0:
            return res
        amount = min(w, capacity)
        res += amount * (v / w)
        capacity -= amount
    return res

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    print("{:.10f}".format(optimal_value(capacity, weights, values)))
