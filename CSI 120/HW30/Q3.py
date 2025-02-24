import os
os.system("cls")

start_num = 1
c = 29
rows = 5

i = 0
while i < rows:
    j = 0
    while j < 5:
        print(start_num + j, end=" ")
        j += 1
    print("\n")
    start_num += c
    c = c * 10 
    i += 1
