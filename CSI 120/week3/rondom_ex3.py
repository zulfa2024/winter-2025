import os
#Check if a Random Number is in a Specific Range
import random

# Define the range
lower_bound = 10
upper_bound = 20

# Generate a random number
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")

# Check if the random number is within the specified range
if lower_bound <= random_number <= upper_bound:
    print(f"The number {random_number} is within the range {lower_bound} to {upper_bound}.")
else:
    print(f"The number {random_number} is not within the range {lower_bound} to {upper_bound}.")
