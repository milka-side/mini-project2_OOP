from sys import stdin
from collections import namedtuple


Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key=lambda x: x.end)
    points = []
    curr_point = -1
    for s in segments:
        if curr_point < s.start:
            curr_point = s.end
            points.append(curr_point)
    return points

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n = data[0]
    segments = [Segment(data[i], data[i+1]) for i in range(1, 2*n, 2)]
    points = optimal_points(segments)
    print(len(points))
    print(*points)
