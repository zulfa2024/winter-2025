# Initialize the matrix and the starting values
matrix = []
start = 1
end = 3

# Use a while loop to generate the matrix
while end <= 7:
    row = list(range(start, end + 1))
    matrix.append(row)
    start += 2
    end += 2

# Print the matrix
for row in matrix:
    print(row)
