
import os
os.system("cls")  
import random

# Randomly generate a number between 1 and 20
target_number = random.randint(1, 20)

# Loop until the user guesses correctly
correct_guess = False
while not correct_guess:
    # Ask the user for a guess
    guess = input("Guess a number between 1 and 20: ")
    
    # Ensure the input is a number
    if guess.isdigit():
        guess = int(guess)
        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            correct_guess = True  # Exit the loop
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")