import sys
import math


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(pts_x, pts_y):
    if len(pts_x) <= 3:
        return min(dist(pts_x[i], pts_x[j]) for i in range(len(pts_x)) for j in range(i+1, len(pts_x)))
    mid = len(pts_x) // 2
    mid_x = pts_x[mid][0]
    d = min(closest_pair(pts_x[:mid], [p for p in pts_y if p[0] < mid_x]),
            closest_pair(pts_x[mid:], [p for p in pts_y if p[0] >= mid_x]))
    strip = [p for p in pts_y if abs(p[0] - mid_x) < d]
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            d = min(d, dist(strip[i], strip[j]))
    return d

if __name__ == '__main__':
    input = sys.stdin.read().split()
    n = int(input[0])
    points = []
    for i in range(n):
        points.append((int(input[2*i+1]), int(input[2*i+2])))
    pts_x = sorted(points, key=lambda p: p[0])
    pts_y = sorted(points, key=lambda p: p[1])
    print("{0:.9f}".format(closest_pair(pts_x, pts_y)))
