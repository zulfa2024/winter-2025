#generate the number and also accept the input from the user. skip out from the loop as soon as random number matches with the number provided by the end user.
import os, random
os.system("cls")
while True:
    #get input from the user
    num = int(input("enter number between 1 to 5: "))
    ranNum = random.randint(1,6)
    if (num == ranNum):
        break
print("random number: ", ranNum)
print("input:", num)
        
              
    

