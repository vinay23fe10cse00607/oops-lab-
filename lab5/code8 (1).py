"""Write a Python program to convert a given list of integers and a tuple of integers in a list of strings."""
def convert_to_strings(int_list, int_tuple):
    return list(map(str, int_list)) + list(map(str, int_tuple))

int_list = [1, 2, 3]
int_tuple = (4, 5, 6)
result = convert_to_strings(int_list, int_tuple)
print(result)  
# Output: ['1', '2', '3', '4', '5', '6']
