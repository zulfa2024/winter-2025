
#Write a program that asks the user to guess a randomly generated number between 1 and 20 (both 1 and 20 are included).
# The program should give hints if the guess is too high or too low and keep asking until the user guesses correctly.
# Once the correct number is guessed, print a congratulatory message.
#don't use function
import os
import random

os.system('cls')

# Generate a random number between 1 and 20
target_number = random.randint(1, 20)

# Ask the user to guess the number
print("Guess the number (between 1 and 20):")

while True:
    try:
        # Ask the user for a guess
        guess = int(input("Enter your guess: "))
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly!")
            break
    except ValueError:
        print("Invalid input! Please enter a number.")
        
        
        

