def evaluate(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b

def get_min_max(i, j, op, m, M):
    min_val = float("inf")
    max_val = float("-inf")
    for k in range(i, j):
        a = evaluate(M[i][k], M[k+1][j], op[k])
        b = evaluate(M[i][k], m[k+1][j], op[k])
        c = evaluate(m[i][k], M[k+1][j], op[k])
        d = evaluate(m[i][k], m[k+1][j], op[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def maximum_value(dataset):
    digits = list(map(int, dataset[0::2]))
    ops = dataset[1::2]
    n = len(digits)
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = get_min_max(i, j, ops, m, M)
    return M[0][n-1]

if __name__ == "__main__":
    print(maximum_value(input()))
