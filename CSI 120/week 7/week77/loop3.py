import os
# Initialize the starting values
start = 1
increment = 10
rows = 5
cols = 5

# Initialize the row counter
row_counter = 0

# Loop to generate the matrix
while row_counter < rows:
    # Initialize the column counter
    col_counter = 0
    # Generate and print each row
    while col_counter < cols:
        print(start + col_counter, end=" ")
        col_counter += 1
    print()  # Move to the next line after each row
    # Update the start value for the next row
    start *= increment
    # Increment the row counter
    row_counter += 1
