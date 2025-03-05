import os

os.system("cls")

#create a tuple

my_tuple = (1,2,3,4,5)

print(my_tuple)

#create empty tuple

empty_tuple = ()



#Tuple with one element

single_tuple = ("10",)

print(type(single_tuple))

#without comma

single_tuple = ("10")

print(type(single_tuple))

#Tuple with Different Data Types

mixed_tuple = (10,"hello",3.14,True)

#tuple without parenetheses

tuple_packed  =1,2,3,"Python"

print(tuple_packed)

#accessing tutples

numbers = (10,20,230,40,60,70)

print(id(numbers))

print(numbers[0])



#negative indexing

print(numbers[-1])

#slicing tuple

print(numbers[1:3])

a = numbers[1:3]

print(a)

print(type(a))

print(numbers[:2])

print(numbers[::2])

#Tuple immutability

#numbers[0]=20

numbers = ("Eric",50,"Renton")

print(id(numbers))

num = 10

print(id(num))

num=20

print(id(num))

# my_tuple[0] = 100  # This will cause an error!

# if a tuple contains a mutable object (e.g., a list),

nested_tuple=(1,2,[3,4])

print(nested_tuple[0])

print(nested_tuple[2][0])

nested_tuple[2][0] = 70

print(nested_tuple)

#Concatenation

tuple1 = (1,2,3)

tuple2=(4,5,6)

result = tuple2+tuple1

print(result)



#repitition

repeat_tuple = ("Python",)*3

print(repeat_tuple)

#Membership Test

if 5 not in tuple1:

    print("it is not part of tuple 1")

else:

    print("it is part of tuple 1")

#count()- Counts occurrences of an element

my_tuple = (1,2,3,1,1,1,2,3,1)

print(my_tuple.count(111))

# index()- Finds the first occurrence of an element

print(my_tuple.index(3))



#What if item does not exist

if 30 in my_tuple:

    print(my_tuple.index(3))

else:

    print("item does not exist")

#Unpacking Tuples

person=("John",25,"Programmer")

name,age,job=person

print(name, age, job)

# Using * for Arbitrary Length Tuples

numbers = (1,2,3,4,5)

a,*b,c = numbers

print(a,b,c)

print(type(a),type(b),type(c))

#convert list b to tuple b

b = tuple(b)

print(type(b))



#Converting Between Tuples and Lists

#tuple to list

tuple_data = (1,2,3)

list_data = list(tuple_data)

list_data[0]=100

print(list_data)

print(type(list_data))

#list to tuple



# loop through tuples

my_tuple = ("apple","bannana","Cherry")

for mt in my_tuple:

    print(mt)

    print("***********")

# loops with index 

    for i in range(len(my_tuple)):

        print(my_tuple[i])

 

#loops using while

        print("***********")

i=0

while i < len(my_tuple):

    print(my_tuple[i])

    i +=1




#workaround to update the tuple 

cars = ("honda", "tesla", "BMW")

cars_list = list(cars)

cars_list[1] = "Honda Civic"

cars_list.append("Porsche")

cars = tuple(cars_list)

print(cars)

print(type(cars))

#workaround to add item(s) to the tuple 



#List of Tuples and Looping Through Them

employees  = [

    ("Roy",49,"Seattle"),

    ("Bob",22,"Bellevue"),

    ("Shane",29,"Renton")

]

for employee in employees:

    name,age,city = employee

    print(f"Name: {name};Age: {age}; City: {city}\n")
    
    


