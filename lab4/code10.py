"""Write a program to check whether a given Number is Palindrome or Not."""
def is_palindrome(num):
    """Checks if a given number is a Palindrome."""

    return str(num) == str(num)[::-1]

# Example usage:
number = 121
if is_palindrome(number):
    print(f"{number} is a Palindrome.")
else:
    print(f"{number} is not a Palindrome.")