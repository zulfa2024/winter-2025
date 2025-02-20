import os
num = int(input("enter number: "))
while num /10>0:   #67
    print(num%10,end="")
    num = int(num/10)  #num = 6