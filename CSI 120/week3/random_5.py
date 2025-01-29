import os
#Find the Largest of Three Random Numbers
import random

# Generate three random numbers between 1 and 100
number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
number3 = random.randint(1, 100)

print(f"The random numbers are: {number1}, {number2}, {number3}")

# Find the largest number
largest = max(number1, number2, number3)

print(f"The largest number is: {largest}")
