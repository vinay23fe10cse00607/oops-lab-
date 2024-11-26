"""Write a Python program to listify the list of given strings individually using Python map."""
def listify_strings(strings):
    return list(map(list, strings))

strings = ["hello", "world"]
result = listify_strings(strings)
print(result)  
# Output: [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']]
