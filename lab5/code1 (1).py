"""Write a Python program to triple all numbers in a given list of integers. Use Python map."""
def triple_numbers(numbers):
    return list(map(lambda x: x * 3, numbers))

numbers = [1, 2, 3, 4, 5]
result = triple_numbers(numbers)
print(result) 
 # Output: [3, 6, 9, 12, 15]
