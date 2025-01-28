# generate two random numbers between begin and end and compare the numbers
#expected output
#Enter begin of the range: 10
#Enter end of the range: 20
#Generated number-1:7
#generated number-2:9
#number 9 is larger than number 7

import random


begin = int(input("Enter begin of the range: }"))
end =  int(input("Enter begin of the range: }"))
number_1 = random.randint(begin, end)

number_2 = random.randint(begin, end)

number2 = random.randint(begin, end)
print(f"generated no is {number1}")

number_2 = random.randint(begin, end)
print(f"generated no is {number_2}")
print(f"Generated number-1:{number_1}")
     
print("Generated number-2:9", number_2)

if number1 > number_2:
    print("Number", number_1, "is larger than number", number_2)
elif number_2 > number_1:
    print("Number", number_2, "is larger than number", number_1)
else:
    print("Number are equal")
    )

