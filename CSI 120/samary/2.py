import os
os.system("cls")
#variable declared inside
for i in range(5): # 'i' is local variable
    square = i ** 2 # 'square' is local variable
    print(f"Number: {i}, square: {square}")
    
    
print(square)