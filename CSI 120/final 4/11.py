import random

# Generate 10 random integers between 1 and 100 and store them in a list
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

# Print all the numbers
print("Numbers:", numbers)

# Find the largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

# Find the smallest number
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

# Calculate the sum of all the numbers
total_sum = 0
for num in numbers:
    total_sum += num

# Calculate the length of the list
length = 0
for _ in numbers:
    length += 1

# Calculate the average of the numbers
average = total_sum / length

# Print the results
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Sum of Numbers:", total_sum)
print("Average of Numbers:", average)