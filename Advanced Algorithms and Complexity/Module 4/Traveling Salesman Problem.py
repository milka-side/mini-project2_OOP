# python3
import sys


INF = 10**9

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    m = int(input_data[1])
    adj = [[INF] * n for _ in range(n)]
    idx = 2
    for _ in range(m):
        u, v, w = map(int, input_data[idx:idx+3])
        adj[u-1][v-1] = adj[v-1][u-1] = w
        idx += 3
    dp = [[INF] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)): continue
            if dp[mask][u] == INF: continue
            for v in range(n):
                if mask & (1 << v): continue
                if adj[u][v] == INF: continue
                new_mask = mask | (1 << v)
                if dp[new_mask][v] > dp[mask][u] + adj[u][v]:
                    dp[new_mask][v] = dp[mask][u] + adj[u][v]
                    parent[new_mask][v] = u
    full_mask = (1 << n) - 1
    best_dist = INF
    last_node = -1
    for i in range(1, n):
        if dp[full_mask][i] + adj[i][0] < best_dist:
            best_dist = dp[full_mask][i] + adj[i][0]
            last_node = i
    if best_dist >= INF:
        print("-1")
        return
    path = []
    curr_mask = full_mask
    curr_node = last_node
    while curr_node != -1:
        path.append(curr_node + 1)
        prev_node = parent[curr_mask][curr_node]
        curr_mask ^= (1 << curr_node)
        curr_node = prev_node
    print(best_dist)
    print(*(path[::-1]))

if __name__ == '__main__':
    solve()
