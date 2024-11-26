"""Q2. Write a program to perform addition, subtraction, multiplication,
 division on a floating point number and print the result up to two places of decimal.
"""
num1 = 5.25
num2 = 2.50

print(f"Addition: {num1 + num2:.2f}")
## or
print("Subtraction: {:.2f}".format(num1 - num2))
print("Multiplication: {:.2f}".format(num1 * num2))
print("Division: {:.2f}".format(num1 / num2))
"""
Output - 
Addition: 7.75
Subtraction: 2.75
Multiplication: 13.12
Division: 2.10  """