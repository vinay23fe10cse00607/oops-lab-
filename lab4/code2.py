"""Write a program to determine whether the given number is a Harshad Number (If a number is divisible by the sum of its digits, then it will be known as a Harshad Number)."""
def is_harshad_number(num):
    """Checks if a given number is a Harshad Number."""

    sum_of_digits = sum(map(int, str(num)))
    return num % sum_of_digits == 0

# Example usage:
number = 18
if is_harshad_number(number):
    print(f"{number} is a Harshad Number.")
else:
    print(f"{number} is not a Harshad Number.")