import random
num = random.randint(1,10)

print("Guess the number between 1 and 10: ")

guess = int(input("Enter number between 1 to 10"))
print("System generated number: "+str(guess))
if guess == num:
    print("You won")
else:
    print("try again")

