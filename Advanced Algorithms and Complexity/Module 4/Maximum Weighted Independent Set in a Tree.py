# python3
import sys
import threading


sys.setrecursionlimit(200000)
threading.stack_size(2**26)

def solve():
    line1 = sys.stdin.readline()
    if not line1: return
    n = int(line1)
    weights = list(map(int, sys.stdin.readline().split()))
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    D = [[0, 0] for _ in range(n)]
    def dfs(v, p):
        D[v][1] = weights[v]
        D[v][0] = 0
        for u in adj[v]:
            if u == p:
                continue
            dfs(u, v)
            D[v][0] += max(D[u][0], D[u][1])
            D[v][1] += D[u][0]
    if n > 0:
        dfs(0, -1)
        print(max(D[0][0], D[0][1]))
    else:
        print(0)

if __name__ == '__main__':
    threading.Thread(target=solve).start()
