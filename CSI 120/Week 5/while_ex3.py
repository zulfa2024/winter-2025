# display first n prime numbers
# function to check if a number is prime
#5
#7
import os
os.system('cls')
n = int(input('Enter the number of prime numbers to display: '))
count = 0
num = 2

while count < n:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num)
        count += 1
    num += 1
num = int(input('Enter number:'))
i = 2
flag  = False
counter  = int(input("Enter number: "))
count = 0
while count <counter:
    num = 4
    while i<num:
       if num %i ==0:
         flag = True
         break   
       i=i+1    
    if flag == False:
        print("it is not a prime number")
    else:
      print("it is a prime number")