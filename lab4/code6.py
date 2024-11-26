"""Write a program to generate the Fibonacci Series."""
def generate_fibonacci_series(n):
    """Generates the Fibonacci Series up to n terms."""

    if n <= 0:
        return []

    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])

    return fib_series

# Example usage:
n = 10
fib_series = generate_fibonacci_series(n)
print(fib_series)
