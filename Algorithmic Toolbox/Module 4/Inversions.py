def merge_and_count(a, b):
    res = []
    i = j = count = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
            count += (len(a) - i)
    res.extend(a[i:])
    res.extend(b[j:])
    return res, count

def count_inversions(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, left_inv = count_inversions(a[:mid])
    right, right_inv = count_inversions(a[mid:])
    merged, split_inv = merge_and_count(left, right)
    return merged, left_inv + right_inv + split_inv

if __name__ == '__main__':
    import sys
    n, *a = map(int, sys.stdin.read().split())
    _, result = count_inversions(a)
    print(result)
