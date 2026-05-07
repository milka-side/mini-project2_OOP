#python3
import sys


class MaxMatching:
    def __init__(self):
        self.nx = 0
        self.ny = 0
        self.matching_x = []
        self.matching_y = []
        self.visited = []

    def dfs(self, u, adj_matrix):
        for v in range(self.ny):
            if adj_matrix[u][v] and not self.visited[v]:
                self.visited[v] = True
                if self.matching_y[v] == -1 or self.dfs(self.matching_y[v], adj_matrix):
                    self.matching_y[v] = u
                    self.matching_x[u] = v
                    return True
        return False

    def solve(self):
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        self.nx = int(input_data[0])
        self.ny = int(input_data[1])
        adj_matrix = []
        idx = 2
        for i in range(self.nx):
            adj_matrix.append([int(x) == 1 for x in input_data[idx : idx + self.ny]])
            idx += self.ny
        self.matching_x = [-1] * self.nx
        self.matching_y = [-1] * self.ny
        for i in range(self.nx):
            self.visited = [False] * self.ny
            self.dfs(i, adj_matrix)
        print(*(x + 1 if x != -1 else -1 for x in self.matching_x))

if __name__ == '__main__':
    MaxMatching().solve()
