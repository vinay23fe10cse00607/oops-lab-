"""Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer."""
def create_new_list(tuple_data, string_value):
    return list(map(int, tuple_data)) + [int(string_value)]

tuple_data = (1, 2, 3)
string_value = "4"
result = create_new_list(tuple_data, string_value)
print(result)  
# Output: [1, 2, 3, 4]
