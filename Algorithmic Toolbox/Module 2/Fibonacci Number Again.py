def get_pisano_period(m):
    a, b = 0, 1
    for i in range(0, m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1
    return 0

def fibonacci_huge(n, m):
    if n <= 1:
        return n
    period = get_pisano_period(m)
    n = n % period
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % m
    return b

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
