def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    def calculate_gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return (a * b) // calculate_gcd(a, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
