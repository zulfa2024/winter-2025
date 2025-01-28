#Checking if a Random Number is Even or Odd
import os, random

os.system('cls')

# Generate a random number 

number = random.randint (1,100)
print('system generated a random number ='+str(number))
print(f"system generated a random number is {number}")

if number  %2 == 0: #check is number is even. if remainder after dividing a number by 2 is 0 then it is even
    print("The number is even.")
else:
    print("The number is odd.")
