# python3
import sys


sys.setrecursionlimit(2000000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        states = next(it)
    except StopIteration:
        return
    color_map = {
        'R': ('G', 'B'),
        'G': ('R', 'B'),
        'B': ('R', 'G')
    }
    adj = [[] for _ in range(2 * n)]
    for _ in range(m):
        try:
            u = int(next(it)) - 1
            v = int(next(it)) - 1
        except StopIteration:
            break
        u_cols = color_map[states[u]]
        v_cols = color_map[states[v]]
        for bit_u in range(2):
            for bit_v in range(2):
                if u_cols[bit_u] == v_cols[bit_v]:
                    lit_u = 2 * u + bit_u
                    lit_v = 2 * v + bit_v
                    adj[lit_u].append(lit_v ^ 1)
                    adj[lit_v].append(lit_u ^ 1)
    def get_order():
        visited = [False] * (2 * n)
        order = []
        for i in range(2 * n):
            if not visited[i]:
                stack = [(i, 0)]
                while stack:
                    curr, child_idx = stack.pop()
                    if child_idx == 0:
                        if visited[curr]: continue
                        visited[curr] = True
                    if child_idx < len(adj[curr]):
                        stack.append((curr, child_idx + 1))
                        stack.append((adj[curr][child_idx], 0))
                    else:
                        order.append(curr)
        return order[::-1]
    order = get_order()
    adj_rev = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            adj_rev[v].append(u)
    scc = [-1] * (2 * n)
    scc_cnt = 0
    for start_node in order:
        if scc[start_node] == -1:
            stack = [start_node]
            while stack:
                curr = stack.pop()
                if scc[curr] == -1:
                    scc[curr] = scc_cnt
                    for neighbor in adj_rev[curr]:
                        stack.append(neighbor)
            scc_cnt += 1
    res_assignment = [False] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("Impossible")
            return
        res_assignment[i] = scc[2 * i] < scc[2 * i + 1]
    final_colors = []
    for i in range(n):
        idx = 1 if res_assignment[i] else 0
        final_colors.append(color_map[states[i]][idx])
    print("".join(final_colors))

if __name__ == "__main__":
    solve()
