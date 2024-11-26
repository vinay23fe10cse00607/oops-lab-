"""Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map."""
def power_list(base, length):
    return list(map(lambda x: base ** x, range(length)))

base = 2
length = 5
result = power_list(base, length)
print(result)  
# Output: [1, 2, 4, 8, 16]
