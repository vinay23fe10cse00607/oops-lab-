def print_pattern(n):

    for i in range(1, n + 1):
        for j in range(i * (i - 1) // 2 + 1, i * (i + 1) // 2 + 1):
            print(j, end=" ")
        print()

# Example usage:
n = 4
print_pattern(n)
#Output -
"""
1 
2 3 
4 5 6 
7 8 9 10 

"""