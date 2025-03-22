
#Write a Python program that prints a multiplication table for numbers from 1 to 10.

#The program should use nested loops to generate and display the table shown below:

import os

os.system("cls")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print() 
    
