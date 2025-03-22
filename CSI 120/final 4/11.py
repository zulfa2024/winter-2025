#Prompts the user to input a list of 5 tuples, where each tuple contains a name and an age (e.g., ("Alice", 20)). 
#The program should check if anyone is above 18 years old and print their name.
import os

os.system('cls')

# Prompt the user to input the 5 tuples (name, age)
print("Please enter 5 tuples, each containing a name and an age.")
people = []

for i in range(5):
    name = input(f"Enter name for person {i + 1}: ")
    age = int(input(f"Enter age for person {i + 1}: "))
    people.append((name, age))

# Check if anyone is above 18 years old
print("\nPeople above 18 years old:")

for person in people:
    if person[1] > 18:
        print(person[0])
        


 
    