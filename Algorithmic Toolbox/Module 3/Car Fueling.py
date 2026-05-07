def min_refills(distance, tank, stops):
    stops = [0] + stops + [distance]
    num_refills, curr = 0, 0
    while curr < len(stops) - 1:
        last = curr
        while curr < len(stops) - 1 and stops[curr + 1] - stops[last] <= tank:
            curr += 1
        if curr == last:
            return -1
        if curr < len(stops) - 1:
            num_refills += 1
    return num_refills

if __name__ == '__main__':
    import sys
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(min_refills(d, m, stops))
