def get_fibonacci_last_digit(n):
    n = n % 60
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
    return b

def fibonacci_sum_squares(n):
    last_digit_n = get_fibonacci_last_digit(n)
    last_digit_n_plus_1 = get_fibonacci_last_digit(n + 1)
    return (last_digit_n * last_digit_n_plus_1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
