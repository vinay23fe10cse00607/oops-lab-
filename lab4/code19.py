def pascal_triangle(n):
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1)
        print(" " * (n - i), end="")
        print(" ".join(map(str, row)))
        prev_row = row

n = int(input("Enter the number of rows: "))
pascal_triangle(n)
#Outut-
"""
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1

"""