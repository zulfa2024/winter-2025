# Initialize the matrix
matrix = []

# Starting value
start_value = 1

# Number of rows in the matrix
num_rows = 3

# Number of columns in the matrix
num_cols = 3

# Loop through each row
for row_index in range(num_rows):
    # Create a new row
    row = []
    
    # Set the value for the first column in the row
    current_value = start_value
    
    # Loop through each column
    for col_index in range(num_cols):
        # Append the value to the row
        row.append(current_value)
        
        # Update the current value for the next column
        current_value += 1
    
    # Append the row to the matrix
    matrix.append(row)
    
    # Update the starting value for the next row
    start_value += 2

# Print the matrix
for row in matrix:
    print(row)
