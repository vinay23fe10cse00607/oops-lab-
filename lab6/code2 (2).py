"""Wapp to pass the list as an argument in the fn"""
def process_list(input_list):
    return [x * 2 for x in input_list]

my_list = [1, 2, 3, 4]
result = process_list(my_list)
print(result)
# Output: [2, 4, 6, 8]
