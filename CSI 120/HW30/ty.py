#write a program to display total 20 natural numbers(starting from number 1) that are not divisible by number 5
import os
os.system("cls")
counter = 0
num = 0
total = 30
while counter < total:
    if num % 5 == 0:
        counter += 1
        num += 1
        continue
    print(num,end = " ")
    counter += 1
    num += 1
print("\ntotal numbers: ",counter)
    

           

