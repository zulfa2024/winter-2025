
# Program to print the day of the week based on user input

# Dictionary mapping numbers to days of the week
days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

# Ask the user to enter a number
number = input("Enter a number between 1 and 7: ")

if number.isdigit():
    number = int(number)
    if 1 <= number <= 7:
        print("The day of the week is " + days_of_week[number] + ".")
    else:
        print("Error: Please enter a number between 1 and 7.")
else:
    print("Error: Invalid input. Please enter a numeric value.")