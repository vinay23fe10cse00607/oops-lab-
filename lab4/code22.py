def display_pattern(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            print('1' + '01' * (i // 2))
        else:
            print('01' * (i // 2))

num_lines = int(input("Enter the number of lines: "))
display_pattern(num_lines)
#Output -
"""
1
01
101
0101
10101
"""