def optimal_summands(n):
    summands = []
    curr = 1
    while n > 0:
        if n <= 2 * curr:
            summands.append(n)
            break
        summands.append(curr)
        n -= curr
        curr += 1
    return summands

if __name__ == '__main__':
    n = int(input())
    res = optimal_summands(n)
    print(len(res))
    print(*res)
