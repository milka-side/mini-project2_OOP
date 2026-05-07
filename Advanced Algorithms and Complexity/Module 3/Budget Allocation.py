# python3
import sys


def print_equisatisfiable_sat_formula():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    A = []
    idx = 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input_data[idx]))
            idx += 1
        A.append(row)
    b = []
    for i in range(n):
        b.append(int(input_data[idx]))
        idx += 1
    clauses = []
    for i in range(n):
        row = A[i]
        limit = b[i]
        non_zero_indices = [j for j, val in enumerate(row) if val != 0]
        num_non_zero = len(non_zero_indices)
        for j in range(1 << num_non_zero):
            current_sum = 0
            for bit in range(num_non_zero):
                if (j >> bit) & 1:
                    current_sum += row[non_zero_indices[bit]]
            if current_sum > limit:
                clause = []
                for bit in range(num_non_zero):
                    var_idx = non_zero_indices[bit] + 1
                    if (j >> bit) & 1:
                        clause.append(-var_idx)
                    else:
                        clause.append(var_idx)
                if clause:
                    clauses.append(" ".join(map(str, clause)) + " 0")
    if not clauses:
        print("1 1")
        print("1 -1 0")
    else:
        print("{0} {1}".format(len(clauses), m))
        print("\n".join(clauses))

if __name__ == "__main__":
    print_equisatisfiable_sat_formula()
