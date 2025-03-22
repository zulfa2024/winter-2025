
import random

# Generate 10 random integers between 1 and 100 and store them in a list
numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 100))

# Print all the numbers
print("The numbers are:", numbers)

# Find the largest number in the list manually
largest_number = numbers[0]
for num in numbers:
    if num > largest_number:
        largest_number = num
print("The largest number is:", largest_number)

# Find the smallest number in the list manually
smallest_number = numbers[0]
for num in numbers:
    if num < smallest_number:
        smallest_number = num
print("The smallest number is:", smallest_number)

# Calculate the sum of all the numbers manually
total_sum = 0
for num in numbers:
    total_sum += num
print("The sum of the numbers is:", total_sum)

# Calculate the average manually
count = 0
for _ in numbers:
    count += 1
average = total_sum / count
print("The average of the numbers is:", average)