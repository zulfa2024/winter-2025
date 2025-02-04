# Display first n prime numbers
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

# Check if a specific number is prime
num_to_check = int(input('Enter a number to check if it is prime: '))
i = 2
is_prime = True

while i * i <= num_to_check:
    if num_to_check % i == 0:
        is_prime = False
        break
    i += 1

if is_prime and num_to_check > 1:
    print(f"{num_to_check} is a prime number")
else:
    print(f"{num_to_check} is not a prime number")

    
