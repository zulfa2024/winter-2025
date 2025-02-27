import os

os.system("cls")   
#WRITE A PROGRAM to display first 20 natural numbers. skips all the numbers that are divisible by 5.
for i in range(1,21):
    if i%5==0:
        continue
    print(i, end=" ")  