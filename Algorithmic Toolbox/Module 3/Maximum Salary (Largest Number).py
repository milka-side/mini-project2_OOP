from functools import cmp_to_key


def largest_number(numbers):
    def compare(a, b):
        if a + b > b + a:
            return -1
        return 1
    numbers.sort(key=cmp_to_key(compare))
    res = "".join(numbers)
    return res if int(res) != 0 else "0"

if __name__ == '__main__':
    import sys
    _ = sys.stdin.readline()
    nums = sys.stdin.readline().split()
    print(largest_number(nums))
