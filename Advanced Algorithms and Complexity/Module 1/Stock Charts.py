#python3
import sys


class StockCharts:
    def solve(self):
        input_data = sys.stdin.read().split()
        if not input_data: return
        n = int(input_data[0])
        k = int(input_data[1])
        stocks = []
        idx = 2
        for i in range(n):
            stocks.append(list(map(int, input_data[idx : idx + k])))
            idx += k
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if all(stocks[i][p] < stocks[j][p] for p in range(k)):
                    adj[i].append(j)
        matching = [-1] * n
        def dfs(u, visited):
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if matching[v] < 0 or dfs(matching[v], visited):
                        matching[v] = u
                        return True
            return False
        result = 0
        for i in range(n):
            if dfs(i, [False] * n):
                result += 1
        print(n - result)

if __name__ == '__main__':
    StockCharts().solve()
