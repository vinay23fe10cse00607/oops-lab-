""" Write a Python program to add three given lists using Python map and lambda."""
def add_lists(list1, list2, list3):
    return list(map(lambda x, y, z: x + y + z, list1, list2, list3))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = add_lists(list1, list2, list3)
print(result)  
# Output: [12, 15, 18]
