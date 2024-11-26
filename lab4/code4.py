"""Write a program to Compute the Value of Xn."""
def calculate_xn(x, n):
    """Calculates the value of Xn."""

    result = x**n
    return result

# Example usage:
x = 2
n = 3
result = calculate_xn(x, n)
print(f"2^3 = {result}")