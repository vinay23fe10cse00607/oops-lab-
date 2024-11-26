"""Write a program to find the reverse of a given number."""
def reverse_number(num):
    """Reverses a given number."""

    reversed_num = int(str(num)[::-1])
    return reversed_num

# Example usage:
number = 12345
reversed_number = reverse_number(number)
print(f"Reversed number of 12345: {reversed_number}")