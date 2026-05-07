def fibonacci_number(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
