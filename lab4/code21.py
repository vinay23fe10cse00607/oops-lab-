def display_pattern(n):
    for i in range(n):
        row = ""
        for j in range(i * 2 + 1):
            if j % 2 == 0:
                row += "A"
            else:
                row += "B"
        print(row)

n = 4
display_pattern(n)
#Output -
"""
A
ABA
ABABA
ABABABA


"""