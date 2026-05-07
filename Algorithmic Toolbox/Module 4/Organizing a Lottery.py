import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    events = []
    for s in starts: events.append((s, 1)) # Початок
    for e in ends:   events.append((e, 3)) # Кінець
    for i, p in enumerate(points): events.append((p, 2, i))
    events.sort()
    active_segments = 0
    for e in events:
        if e[1] == 1: active_segments += 1
        elif e[1] == 3: active_segments -= 1
        elif e[1] == 2: cnt[e[2]] = active_segments
    return cnt

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    starts = data[2:2*n+2:2]
    ends = data[3:2*n+2:2]
    points = data[2*n+2:]
    print(*fast_count_segments(starts, ends, points))
