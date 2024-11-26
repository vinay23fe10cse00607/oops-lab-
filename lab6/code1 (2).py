"""⁠Wapp to use various inbuilt fn of list"""
def list_inbuilt_functions_demo():
    # Creating a sample list
    my_list = [5, 2, 9, 1, 5, 6]
    print("Original List:", my_list)

    # Append: Add an item to the end of the list
    my_list.append(7)
    print("After Append (7):", my_list)

    # Extend: Extend the list by appending elements from another iterable
    my_list.extend([8, 10])
    print("After Extend ([8, 10]):", my_list)

    # Insert: Insert an item at a given position
    my_list.insert(2, 4)
    print("After Insert (4 at index 2):", my_list)

    # Remove: Remove the first occurrence of a value
    my_list.remove(5)
    print("After Remove (first occurrence of 5):", my_list)

    # Pop: Remove and return an item at the given position (default last)
    popped_item = my_list.pop()
    print("After Pop (removed item):", my_list)
    print("Popped Item:", popped_item)

    # Count: Count the occurrences of a value
    count_of_five = my_list.count(5)
    print("Count of 5 in the list:", count_of_five)

    # Sort: Sort the items of the list in place
    my_list.sort()
    print("After Sort:", my_list)

    # Reverse: Reverse the elements of the list in place
    my_list.reverse()
    print("After Reverse:", my_list)

    # Index: Return the index of the first occurrence of a value
    index_of_one = my_list.index(1)
    print("Index of 1 in the list:", index_of_one)

    # Slicing: Get a slice of the list
    slice_of_list = my_list[1:4]
    print("Slice of List (index 1 to 4):", slice_of_list)

    # Length: Get the number of items in the list
    length_of_list = len(my_list)
    print("Length of the List:", length_of_list)

# Example usage
list_inbuilt_functions_demo()