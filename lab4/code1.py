"""Write a program program to check if the given number is a Disarium Number (11+ 72 + 53 = 1+ 49 + 125 = 175)."""
def is_disarium_number(num):
    """Checks if a given number is a Disarium Number."""

    sum_of_digits = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** (len(str(num)) - 1)
        temp //= 10

    return sum_of_digits == num

# Example usage:
number = 175
if is_disarium_number(number):
    print(f"{number} is a Disarium Number.")
else:
    print(f"{number} is not a Disarium Number.")
#Output- 
"""175 is not a Disarium Number. """