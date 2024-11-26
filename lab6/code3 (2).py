"""Wapp to take variable length arguments in fn and perform cube of each elements """
def cube_elements(*args):
    return [x ** 3 for x in args]

result = cube_elements(1, 2, 3, 4)
print(result)
# Output: [1, 8, 27, 64]
