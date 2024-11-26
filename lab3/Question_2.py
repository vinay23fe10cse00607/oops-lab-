"""Q2. WAP to find the given number is palindrome or not."""
number = input("Enter a number: ")

reversed_number = number[::-1]

if number == reversed_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
"""Output-
Enter a number: 121
121 is a palindrome. """