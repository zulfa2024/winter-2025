#print multiplication table like:
'''
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
'''
import os

os.system("cls")

for i in range(1, 6):
    for j in range(1, 6): # i = 1, j = 1
        print(i*j, end =" ")
    print()