# python3
import sys


class HamiltonianPathToSAT:
    def __init__(self, n, m):
        self.vertices_num = n
        self.matrix = [[False] * n for _ in range(n)]
        self.data = [[0] * n for _ in range(n)]
        cnt = 1
        for i in range(n):
            for j in range(n):
                self.data[i][j] = cnt
                cnt += 1
        self.clauses = []

    def add_edge(self, u, v):
        self.matrix[u-1][v-1] = True
        self.matrix[v-1][u-1] = True

    def each_vertex_in_path(self):
        for i in range(self.vertices_num):
            clause = [self.data[i][j] for j in range(self.vertices_num)]
            self.clauses.append(clause)

    def each_vertex_in_path_only_once(self):
        for j in range(self.vertices_num):
            for i in range(self.vertices_num):
                for k in range(i + 1, self.vertices_num):
                    self.clauses.append([-self.data[i][j], -self.data[k][j]])

    def each_path_position_occupied(self):
        for j in range(self.vertices_num):
            clause = [self.data[i][j] for i in range(self.vertices_num)]
            self.clauses.append(clause)

    def vertices_occupy_diff_positions(self):
        for i in range(self.vertices_num):
            for j in range(self.vertices_num):
                for k in range(j + 1, self.vertices_num):
                    self.clauses.append([-self.data[i][j], -self.data[i][k]])

    def nonadjacent_vertices_nonadjacent_in_path(self):
        for i in range(self.vertices_num):
            for j in range(i + 1, self.vertices_num):
                if not self.matrix[i][j]:
                    for k in range(self.vertices_num - 1):
                        self.clauses.append([-self.data[i][k], -self.data[j][k+1]])
                        self.clauses.append([-self.data[j][k], -self.data[i][k+1]])

    def solve(self):
        self.each_vertex_in_path()
        self.each_vertex_in_path_only_once()
        self.each_path_position_occupied()
        self.vertices_occupy_diff_positions()
        self.nonadjacent_vertices_nonadjacent_in_path()
        print("{0} {1}".format(len(self.clauses), self.vertices_num * self.vertices_num))
        for clause in self.clauses:
            print(" ".join(map(str, clause)) + " 0")

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    converter = HamiltonianPathToSAT(n, m)
    curr = 2
    for _ in range(m):
        u = int(input_data[curr])
        v = int(input_data[curr+1])
        converter.add_edge(u, v)
        curr += 2
    converter.solve()

if __name__ == "__main__":
    main()
