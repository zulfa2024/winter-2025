
import os

# Clear the screen
os.system("cls")
# Multiplication table for numbers 1 to 10

# Outer loop for rows (1 to 10)
i = 1
while i <= 10:
    # Inner loop for columns (1 to 10)
    j = 1
    while j <= 10:
        print(f"{i * j:4}", end="")  # Print each product, formatted with a fixed width
        j += 1
    print()  # Move to the next line after each row
    i += 1