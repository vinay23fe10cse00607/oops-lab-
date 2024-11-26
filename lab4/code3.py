"""Write a program to Print Armstrong Number from 1 to 1000."""
def is_armstrong_number(num):
    """Checks if a given number is an Armstrong Number."""

    order = len(str(num))
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    return sum_of_powers == num

def print_armstrong_numbers(start, end):
    """Prints Armstrong Numbers within a given range."""

    for num in range(start, end + 1):
        if is_armstrong_number(num):
            print(num)

# Example usage:
print_armstrong_numbers(1, 1000)