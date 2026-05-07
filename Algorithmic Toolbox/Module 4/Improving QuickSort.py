from random import randint


def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            a[i], a[m1] = a[m1], a[i]
            m1 += 1
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
        elif a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
    return m1, m2

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

if __name__ == '__main__':
    import sys
    n, *a = map(int, sys.stdin.read().split())
    randomized_quick_sort(a, 0, n - 1)
    print(*a)
