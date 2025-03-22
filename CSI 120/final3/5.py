
import random

# Generate a random number between 1 and 20
target_number = random.randint(1, 20)

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
            break  # Exit the loop when the guess is correct
    except ValueError:
        print("Invalid input. Please enter a numeric value.")