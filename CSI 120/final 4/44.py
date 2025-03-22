
#Write a program that asks the user to enter a number between 1 and 7 (both 1 and 7 are included).
# The program should print the corresponding day of the week.
# If the number is outside this range, it should print an error message.
import os

os.system('cls')

# Prompt the user to enter a number between 1 and 7
day_number = int(input("Enter a number between 1 and 7: "))
days = ["days"]

# Check if the number is between 1 and 7

if day_number >= 1 and day_number <= 7:
    # Print the corresponding day of the week
    print(f"The corresponding day of the week is {days[day_number - 1]}")
else:
    # Print an error message
    print("Error: The number is outside the range 1-7.")
    