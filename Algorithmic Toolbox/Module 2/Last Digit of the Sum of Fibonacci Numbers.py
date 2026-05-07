def fibonacci_sum(n):
    if n <= 1:
        return n
    n = (n + 2) % 60
    if n <= 1:
        return (n - 1 + 10) % 10
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
    return (b - 1 + 10) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
