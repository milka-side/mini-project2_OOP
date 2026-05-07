# python3
import sys


def solve_ad():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n, m = int(input_data[0]), int(input_data[1])
    A = []
    idx = 2
    for _ in range(n):
        A.append(list(map(float, input_data[idx:idx+m])))
        idx += m
    b = [float(x) for x in input_data[idx:idx+n]]
    idx += n
    c = [float(x) for x in input_data[idx:idx+m]]
    num_vars = m
    num_slack = n
    tableau = []
    for i in range(n):
        slack_part = [0.0] * num_slack
        slack_part[i] = 1.0
        tableau.append(A[i] + slack_part + [b[i]])
    objective_row = [-x for x in c] + [0.0] * (num_slack + 1)
    tableau.append(objective_row)
    while True:
        pivot_col = 0
        min_val = tableau[-1][0]
        for j in range(1, num_vars + num_slack):
            if tableau[-1][j] < min_val:
                min_val = tableau[-1][j]
                pivot_col = j
        if min_val >= -1e-9:
            break
        pivot_row = -1
        min_ratio = float('inf')
        for i in range(n):
            if tableau[i][pivot_col] > 1e-9:
                ratio = tableau[i][-1] / tableau[i][pivot_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i
        if pivot_row == -1:
            print("Infinity")
            return
        pivot_val = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [x / pivot_val for x in tableau[pivot_row]]
        for i in range(len(tableau)):
            if i != pivot_row:
                factor = tableau[i][pivot_col]
                for j in range(len(tableau[0])):
                    tableau[i][j] -= factor * tableau[pivot_row][j]
    results = [0.0] * m
    for j in range(m):
        col = [tableau[i][j] for i in range(n)]
        if col.count(1.0) == 1 and sum(col) == 1.0:
            row_idx = col.index(1.0)
            results[j] = tableau[row_idx][-1]
    print("Bounded solution")
    print(*(f"{x:.18f}" for x in results))

if __name__ == "__main__":
    solve_ad()
