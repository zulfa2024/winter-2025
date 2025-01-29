import os
#Checking the age eligibility to work
# Function to check age eligibility
def check_age_eligibility(age):
    if age < 0:
        print("Invalid age")
    elif age < 16:
        print("Not eligible to work")
    else:
        print("Eligible to work")

# Example usage
age = int(input("Enter your age: "))
check_age_eligibility(age)
