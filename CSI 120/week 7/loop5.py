import os
#Reverse a number


import os
import random
os.system('cls')

num = int(input("Enter number: "))  
str_var = ''
while num/10 > 0:
    rev_num = num % 10
    str_var =  str_var + str(rev_num)
    num = int(num/10)
   
print(str_var)
 