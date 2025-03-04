# mutable vs. immutable data structures
import os
os. system ("cls")
num = 10
print (f"Id for num = {id(num)}")
num = 20
print (f"Id for num = {id(num)}")
l_1=[1,2,3,4,5]
print (f"Id for l_1 = {id(l_1)}")
l_1[0] = 10
print(l_1)
print(f"id for l_1 = {id(l_1)}")
l_2 = l_1
l_2[0] = 300
print (l_1,l_2)
print(f"id for l_2 = {id(l_1)} Id for l_2 = {id(l_2)}")
#shallow copy
l_3 = l_1.copy() 
l_3[2] =110

print (l_1,l_3)

print(f"id for l_1 = {id(l_1)} Id for l_3 = {id(l_3)}")



       
       
