def compute_operations(n):
    min_ops = [0] * (n + 1)
    for i in range(2, n + 1):
        ops = [min_ops[i - 1] + 1]
        if i % 2 == 0:
            ops.append(min_ops[i // 2] + 1)
        if i % 3 == 0:
            ops.append(min_ops[i // 3] + 1)
        min_ops[i] = min(ops)
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and min_ops[n] == min_ops[n // 3] + 1:
            n //= 3
        elif n % 2 == 0 and min_ops[n] == min_ops[n // 2] + 1:
            n //= 2
        else:
            n -= 1
    return reversed(sequence)

if __name__ == '__main__':
    import sys
    input_n = int(sys.stdin.read())
    output_sequence = list(compute_operations(input_n))
    print(len(output_sequence) - 1)
    print(*output_sequence)
