def print_pattern_5(n):

    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

# Example usage:
n = 5
print_pattern_5(n)
"""
12345
1234
123
12
1

"""