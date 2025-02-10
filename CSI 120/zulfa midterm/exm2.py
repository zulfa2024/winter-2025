import random

# Generate the lottery number
lottery_num = random.randint(10, 99)

# Get the player's guess
guess = int(input("Enter your 2-digit lottery guess (10-99): "))

# Check the guess and determine the reward
if lottery_num == guess:
    result = "Congratulations! You won $10,000!"
elif sorted(str(lottery_num)) == sorted(str(guess)):
    result = "Great job! You won $5,000!"
elif (str(guess)[0] in str(lottery_num)) or (str(guess)[1] in str(lottery_num)):
    result = "Good try! You won $1,000!"
else:
    result = "Sorry, better luck next time!"

# Display the result
print(f"Lottery number was: {lottery_num}")
print(result)
