import os
os.system("cls")
#Create a program in python using while loop to replicate the following matrix 
counter = 0
num = int(input("enter starting number:"))
total = int(input("enter total count:"))
while counter < total:
    if num % 5 == 0:
        counter += 1
        num += 1
        continue
    print(num,end = " ")
    counter += 1
    num += 1
print("\ntotal numbers: ",counter)