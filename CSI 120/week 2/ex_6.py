
# Creat a program that accepts user's score and checks if student passed the class. minimum passing score is 73.
#input value:
score = int(input("Enter your score:")) # for example,if the in put is 78 it will be not a number it will be score = 75
# string representation of a number
# so make sure if you are using a number as input, convert it to appropriate data type.

# compare if the input is minimum 73

if score >= 73:
    print("pass: out of 100, student got "+str(score)+" score.")
else:
    print("fail: out of 100 student got" +str(score)+" score")
    
    