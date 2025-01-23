import random
#guess a number 1 to 10

import random

number = random.randint(1,2,3,4,5,6,7,8,9,10)

guess = int(input("Guess a number between 1 to 10: "))

if guess == number:
    print("Congratulations! You guessed the correct number.")
    
else:
    print("Sorry, you guessed the wrong number. The correct number was: ", number)