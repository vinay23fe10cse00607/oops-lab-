"""Write a program to display the following pattern: 
A
BB
CCC
DDDD 
EEEEE

"""
def print_pattern_3(n):

    for i in range(65, 65 + n):
        print(chr(i) * (i - 64))

# Example usage:
n = 5
print_pattern_3(n)