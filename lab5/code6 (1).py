"""Write a Python program to convert all the characters into uppercase and lowercase and
eliminate duplicate letters from a given sequence. Use the map() function."""
def eliminate_duplicates(sequence):
    unique_chars = set(sequence)
    upper_chars = list(map(str.upper, unique_chars))
    lower_chars = list(map(str.lower, unique_chars))
    return upper_chars, lower_chars

sequence = "Hello World"
result = eliminate_duplicates(sequence)
print(result) 
 # Output: (['H', 'E', 'O', 'L', 'R', 'W', 'D'], ['h', 'e', 'o', 'l', 'r', 'w', 'd'])
