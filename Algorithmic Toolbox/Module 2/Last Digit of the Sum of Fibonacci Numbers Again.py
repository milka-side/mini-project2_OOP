import sys


def get_fibonacci_last_digit(n):
    n = n % 60
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
    return b

def fibonacci_partial_sum(from_, to):
    last_digit_to = get_fibonacci_last_digit(to + 2)
    last_digit_from = get_fibonacci_last_digit(from_ + 1)
    return (last_digit_to - last_digit_from + 10) % 10

if __name__ == '__main__':
    input_data = sys.stdin.read()
    if input_data:
        from_, to = map(int, input_data.split())
        print(fibonacci_partial_sum(from_, to))
