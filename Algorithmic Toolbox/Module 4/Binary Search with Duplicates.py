def binary_search(keys, query):
    low, high = 0, len(keys) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if keys[mid] == query:
            result = mid
            high = mid - 1
        elif keys[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return result

if __name__ == '__main__':
    import sys
    input_data = sys.stdin.read().split()
    if input_data:
        num_keys = int(input_data[0])
        input_keys = list(map(int, input_data[1:num_keys + 1]))
        num_queries = int(input_data[num_keys + 1])
        input_queries = list(map(int, input_data[num_keys + 2:]))
        for q in input_queries:
            print(binary_search(input_keys, q), end=' ')
