def binary_search(keys, query):
    low, high = 0, len(keys) - 1
    while low <= high:
        mid = (low + high) // 2
        if keys[mid] == query:
            return mid
        elif keys[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    keys = list(map(int, input[1:n+1]))
    m = int(input[n+1])
    queries = list(map(int, input[n+2:]))
    for q in queries:
        print(binary_search(keys, q), end=' ')
