import os
os.system("cls")

# Initialize starting number and increment values
start_num = 1
c = 49

# Number of rows in the matrix
rows = 5

i = 0
while i < rows:
    j = 0
    while j < 5:
        print(start_num + j, end=" ")
        j += 1
    print("\n")
    
    # Update the starting number for the next row
    start_num += c
    
    # Increment value increases by a factor of 10 minus 1 for the next row
    c*= 10
    i += 1
