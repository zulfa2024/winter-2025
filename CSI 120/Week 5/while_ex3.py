#Display first n prime numbers
# display first n prime numbers
import os
os.system('cls')
num = int(input('Enter number:'))  #13
i = 2
flag  = False
counter  = int(input("Enter number: ")) #10
count = 0
while count <counter:
    num = 4
    while i<num:
       if num %i ==0:
         flag = True
         break   
       i=i+1    
    if flag == True:
        print("it is a prime number")
    else:
      print("it is not a prime number")