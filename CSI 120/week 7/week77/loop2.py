import os
 # Initialize the starting values
start_values = [1, 50, 540, 5440, 54440]
matrix = []

# Iterate through each starting value
for start in start_values:
    row = []
    i = 0
    while i < 5:
        row.append(start + i)
        i += 1
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)
