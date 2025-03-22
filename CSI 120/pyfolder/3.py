
# Program to print the multiplication table from 1 to 10
# Outer loop for rows
import os
os.system("cls") 

for i in range(1, 11):
    # Inner loop for columns
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")
    print()
    
    