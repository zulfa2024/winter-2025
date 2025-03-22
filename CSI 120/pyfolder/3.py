# Program to print the multiplication table from 1 to 10
import os
os.system("cls") 
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")
    print()
    
    