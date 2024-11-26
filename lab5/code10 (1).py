"""Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers."""
def fibonacci_squares(n):
    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return list(map(lambda x: fib(x) ** 2, range(n)))

N = 5
result = fibonacci_squares(N)
print(result)  
# Output: [0, 1, 1, 4, 9]
