#generate two numbers between x and y and accept another range and tell if the generated number is within the range
import os, random
os.system('cls')
#input begin of the range
begin_1 = int(input("enter begin of the range:")) #100

#input end of the range_1
end_1 = int(input("enter end of the range:")) #1000
number = random.randint(begin_1,end_1)
print(f"generated no is {number}")


#input begin of the range 2
begin_2 = int(input("enter begin of the range: ")) #100

#input end of the range_2

end_2 = int(input("enter end of the range:")) #1000

if number >= begin_2 and number <= end_2: # To combine the two expressions, use logical operators
    print("Number is within range")
else:
    print("Number is not within range")

#Enter begin range: 100
#Enter end range: 1000
#number:900

#enter begin range: 1000
#Enter end range: 2000






