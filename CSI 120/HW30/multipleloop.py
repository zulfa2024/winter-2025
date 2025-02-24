import os
os.system("cls")
num = int(input("enter a number: "))
iterations = int(input("enter iterations: "))

for i in range(0, iterations):
    print("red\n")
    for j in range(1, num+1):
        print(j, end = " ")
    print("\n")