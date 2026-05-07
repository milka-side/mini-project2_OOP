# python3
import sys
import threading


sys.setrecursionlimit(200000)
threading.stack_size(2**26)

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    def get_node(lit):
        if lit > 0: return 2 * (lit - 1)
        return 2 * (abs(lit) - 1) + 1
    def neg(node):
        return node ^ 1
    idx = 2
    for _ in range(m):
        u_lit, v_lit = int(data[idx]), int(data[idx+1])
        u, v = get_node(u_lit), get_node(v_lit)
        adj[neg(u)].append(v)
        adj[neg(v)].append(u)
        rev_adj[v].append(neg(u))
        rev_adj[u].append(neg(v))
        idx += 2
    order = []
    visited = [False] * (2 * n)
    def dfs1(u):
        visited[u] = True
        for v in rev_adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    visited = [False] * (2 * n)
    scc = [-1] * (2 * n)
    counter = 0
    def dfs2(u, c):
        scc[u] = c
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs2(v, c)
    for i in reversed(order):
        if not visited[i]:
            dfs2(i, counter)
            counter += 1
    assignment = [None] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("UNSATISFIABLE")
            return
        assignment[i] = scc[2 * i] > scc[2 * i + 1]
    print("SATISFIABLE")
    result = []
    for i in range(n):
        result.append(str(i + 1) if assignment[i] else str(-(i + 1)))
    print(" ".join(result))

if __name__ == '__main__':
    thread = threading.Thread(target=solve)
    thread.start()
