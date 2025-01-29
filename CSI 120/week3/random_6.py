import os
#Simulate a Random Dice Roll and Compare Results
import random
from collections import Counter

def roll_dice():
    return random.randint(1, 6)

# Simulate rolling the dice 50 times
num_rolls = 50
rolls = [roll_dice() for _ in range(num_rolls)]
counts = Counter(rolls)

# Print the number of occurrences for each side
print("Dice Roll Results:")
for value in range(1, 7):
    print(f"Value {value}: {counts[value]} times")

# Compare results
most_common = counts.most_common(1)[0]
print(f"\nThe most frequently rolled value is {most_common[0]} (rolled {most_common[1]} times).")
least_common = min(counts, key=counts.get)
print(f"The least frequently rolled value is {least_common} (rolled {counts[least_common]} times).")
