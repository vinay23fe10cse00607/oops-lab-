"""Write a program to display the following pattern:
1
12
123
1234
12345"""
def print_pattern_1(n):

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

# Example usage:
n = 5
print_pattern_1(n)