# Randomly generate a number between 1 and 20 and prompt the user to guess the number.
import os
os.system("cls")  
import random
target_number = random.randint(1, 20)
correct_guess = False
while not correct_guess:
    guess = input("Guess a number between 1 and 20: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            correct_guess = True  
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")