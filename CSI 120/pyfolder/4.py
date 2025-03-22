# Program to print the day of the week based on user input
import random
import os
os.system('cls')
days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
number = input("Enter a number between 1 and 7: ")
if number.isdigit():
    number = int(number)
    if 1 <= number <= 7:
        print("The day of the week is " + days_of_week[number] + ".")
    else:
        print("Error: Please enter a number between 1 and 7.")
