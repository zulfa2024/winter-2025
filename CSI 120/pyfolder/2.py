import random
import os
os.system('cls')

# Generate 10 random integers between 1 and 100 and store them in a list
numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 100))
print("Numbers:", numbers)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
total_sum = 0
for num in numbers:
    total_sum += num
length = 0
for _ in numbers:
    length += 1
average = total_sum / length
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Sum of Numbers:", total_sum)
print("Average of Numbers:", average)