#Display first n prime numbers
import os
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


    
