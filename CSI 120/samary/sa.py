#a global variable is variable that is declared out side of all functions and loops, making it accessible
#throughout the entire program.

#write a program that uses a global variable total_sum to calculate the sum of the numbers from 1 to n using a loop.
#total_sum = 0
    #Global variable
import os
os.system("cls")
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    total_sum = 0
    total_sum += i # modifying global variable
    print(total_sum)
print("sum:", total_sum)
