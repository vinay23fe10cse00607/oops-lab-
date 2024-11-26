"""Q3. WAP to find the grade of student using given percentage"""
def find_grade(percentage):
  if percentage >= 90:
    return 'A'
  elif percentage >= 80:
    return 'B'
  elif percentage >= 70:
    return 'C'
  elif percentage >= 60:
    return 'D'
  else:
    return 'F' 


# Get the percentage from the user
percentage = float(input("Enter the percentage: "))

# Check if the percentage is valid
if percentage < 0 or percentage > 100:
  print("Invalid percentage. Please enter a value between 0 and 100.")
else:
  # Find and print the grade
  grade = find_grade(percentage)
  print("The grade is:", grade)
  #Output-
  """Enter the percentage: 88
     The grade is: B
  """