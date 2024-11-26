"""Write a program to Check whether a given Number is Perfect Number."""
def is_perfect_number(num):
    """Checks if a given number is a Perfect Number."""

    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_of_divisors == num

# Example usage:
number = 28
if is_perfect_number(number):
    print(f"{number} is a Perfect Number.")
else:
    print(f"{number} is not a Perfect Number.")