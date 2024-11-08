def fibonacci(n: int) -> list:
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# Test case
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3]
