"""Write a Python program to add two given lists and find the difference between them. Use the map() function."""
def add_and_difference(list1, list2):
    added = list(map(lambda x, y: x + y, list1, list2))
    difference = list(map(lambda x, y: x - y, list1, list2))
    return added, difference

list1 = [5, 6, 7]
list2 = [1, 2, 3]
added, difference = add_and_difference(list1, list2)
print("Added:", added)  
# Output: [6, 8, 10]
print("Difference:", difference)  
# Output: [4, 4, 4]
