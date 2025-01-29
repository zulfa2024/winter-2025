import os
#Check If a Number is Even and Greater Than 10
def check_number(number):
    if number > 10 and number % 2 == 0:
        return f"{number} is even and greater than 10"
    else:
        return f"{number} is not both even and greater than 10"

# Example usage
number_to_check = 14
result = check_number(number_to_check)
print(result)
