# python3
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n, m = int(input_data[0]), int(input_data[1])
    A = []
    idx = 2
    for _ in range(n):
        A.append([float(x) for x in input_data[idx:idx+m]])
        idx += m
    b = [float(x) for x in input_data[idx:idx+n]]
    idx += n
    c = [float(x) for x in input_data[idx:idx+m]]
    table = []
    for i in range(n):
        slack = [0.0] * n
        slack[i] = 1.0
        table.append(A[i] + slack + [b[i]])
    table.append([-x for x in c] + [0.0] * (n + 1))
    rows = len(table)
    cols = len(table[0])
    while True:
        p_col = -1
        min_val = -1e-9
        for j in range(cols - 1):
            if table[-1][j] < min_val:
                min_val = table[-1][j]
                p_col = j
        if p_col == -1: break
        p_row = -1
        min_ratio = float('inf')
        for i in range(rows - 1):
            if table[i][p_col] > 1e-9:
                ratio = table[i][-1] / table[i][p_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    p_row = i
        if p_row == -1:
            print("Infinity")
            return
        pivot_element = table[p_row][p_col]
        table[p_row] = [x / pivot_element for x in table[p_row]]
        for i in range(rows):
            if i != p_row:
                factor = table[i][p_col]
                for j in range(cols):
                    table[i][j] -= factor * table[p_row][j]
    results = [0.0] * m
    for j in range(m):
        column = [table[i][j] for i in range(rows - 1)]
        if column.count(1.0) == 1 and sum(column) == 1.0:
            row_idx = column.index(1.0)
            results[j] = table[row_idx][-1]
    if any(r < -1e-9 for r in results):
        print("No solution")
    else:
        print("Bounded solution")
        print(*(f"{x:.18f}" for x in results))

if __name__ == "__main__":
    solve()
