#python3
import sys


NO_UNIQUE_SOLUTIONS_MSG = 'No unique solutions'
NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

def first_nonzero_index(iterable, eps=1e-10):
    for k, item in enumerate(iterable):
        if abs(item) > eps:
            return k
    raise Exception(NO_NONZERO_ELTS_FOUND_MSG)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    matrix = []
    b = []
    idx = 1
    for i in range(n):
        row = [float(x) for x in input_data[idx : idx + n]]
        matrix.append(row)
        b.append(float(input_data[idx + n]))
        idx += n + 1
    for i in range(n):
        if abs(matrix[i][i]) < 1e-10:
            for j in range(i + 1, n):
                if abs(matrix[j][i]) > 1e-10:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    b[i], b[j] = b[j], b[i]
                    break
            else:
                print(NO_UNIQUE_SOLUTIONS_MSG)
                return
        pivot = matrix[i][i]
        matrix[i] = [x / pivot for x in matrix[i]]
        b[i] /= pivot
        for j in range(i + 1, n):
            factor = matrix[j][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
            b[j] -= factor * b[i]
    for i in range(n):
        try:
            first_nonzero_index(matrix[i])
        except Exception as e:
            if str(e) == NO_NONZERO_ELTS_FOUND_MSG and abs(b[i]) > 1e-10:
                print(NO_UNIQUE_SOLUTIONS_MSG)
                return
    ans = [0.0] * n
    for i in range(n - 1, -1, -1):
        current_sum = sum(matrix[i][j] * ans[j] for j in range(i + 1, n))
        ans[i] = b[i] - current_sum
    for x in ans:
        print("%.20f" % x)

if __name__ == "__main__":
    solve()
