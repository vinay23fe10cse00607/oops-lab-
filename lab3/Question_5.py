#Q5. Write a program that takes the user's full name, their father's name, and registration number as a single input string and then prints the middles name of the user.
a = input("Enter your name, your father's name, and your reg no.: ")

firstname = ""
middlename = ""
lastname = ""
x = 0
while x < len(a) and a[x] != ' ':
    firstname += a[x]
    x += 1
x += 1
while x < len(a) and a[x] != ' ':
    middlename += a[x]
    x += 1
x += 1
while x < len(a) and x < len(a):
    lastname += a[x]
    x += 1

print("Middle Name:", middlename)