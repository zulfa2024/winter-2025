
#Write a Python program that generates 10 random integers between 1 and 100. The program should do the following:
# 1. Store these numbers in a list.
# 2. Print all the numbers.
# 3. Find and print the largest number in the list.
# 4. Find and print the smallest number in the list.
# 5. Calculate and print the sum of all the numbers.
# 6. Calculate and print the average of the numbers.
import os
import random

os.system("cls")

numbers = [random.randint(1, 100) for _ in range(10)]

print("Generated numbers:")

for number in numbers:
    print(number, end=" ")

print("\nLargest number:", max(numbers))

print("Smallest number:", min(numbers))

print("Sum of numbers:", sum(numbers))

print("Average of numbers:", sum(numbers) / len(numbers))


