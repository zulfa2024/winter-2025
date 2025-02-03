#display first n odd natural numbers 
#1
#3
#5
import os
os.system('cls')
loop_number = int(input("Enter n: "))
counter = 1
count=1
while count <=loop_number:
    print(counter)
    counter =counter+2
    count = count+1