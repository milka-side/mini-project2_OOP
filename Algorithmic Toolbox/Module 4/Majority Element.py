def get_majority_element(a):
    candidate = None
    count = 0
    for x in a:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    if a.count(candidate) > len(a) / 2:
        return 1
    return 0

if __name__ == '__main__':
    import sys
    n, *a = map(int, sys.stdin.read().split())
    print(get_majority_element(a))
