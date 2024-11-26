"""Wapp that accept string and calculate the number of uppercase and lowercase letters in the string """
def count_case(string):
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    print(f"Uppercase : {upper_count} , lowercase : {lower_count}")
    return upper_count, lower_count
    
    

result = count_case("Hello World!")
print(result)
# Output: Uppercase: 2, Lowercase: 8