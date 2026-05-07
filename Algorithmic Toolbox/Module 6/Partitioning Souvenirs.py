def partition3(values):
    total = sum(values)
    if total % 3 != 0 or len(values) < 3:
        return 0
    target = total // 3
    n = len(values)
    dp = {(0, 0)}
    for v in values:
        new_dp = set()
        for s1, s2 in dp:
            if s1 + v <= target:
                new_dp.add((s1 + v, s2))
            if s2 + v <= target:
                new_dp.add((s1, s2 + v))
            new_dp.add((s1, s2))
        dp = new_dp
    return 1 if (target, target) in dp else 0

if __name__ == '__main__':
    import sys
    n, *values = list(map(int, sys.stdin.read().split()))
    print(partition3(values))
