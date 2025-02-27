import os
# Create a list

import os

os.system("cls")

# Add cars in cars list variabe: "BMW", "Ferrari","Fiat", "Honda"

cars = ["BMW", "Ferrari","Fiat", "Honda"]

print(cars)

#append Item in list: "Audi"

cars.append("Audi")



#print cars

print(cars)

#display length(no. of items) of the list

print("*****Print number of items in the list*****")

length = len(cars)

print("*****Print content using for loop*****")

print(length)

for i in range(length):

    print(cars[i])                #cars[0] = BMW, cars[1]=Ferrari, cars[2]=Fiat,cars[3]=Honda, cars[4] = AUdi



print("*********display list items using for loop (another version)*************")

# display list items using for loop (another version)

for car in cars:

    print(car)



# display list items using while loop

print("*****Print content using while loop*****")

counter = 0

while counter <length:

    print(cars[counter])

    counter +=1



#sort list

cars.sort()

print("******** Sorted List") 

print(cars)

# sort list in descending order

print("*****Print list in descending order*****")

cars.sort(reverse=True)

print(cars)



print(cars)

# Reverse the list

list_num = [1,2,3,49,2]

list_num.reverse()   #reverse_list = list_num.reverse()

print(list_num)



# Copy the list

print("*****Copy List***********")

copy_list = list_num.copy()

print(copy_list)

# Remove the last item using pop

print("*****Remove last items fromcars_copy List***********")



deleted_item = list_num.pop()

print(list_num)

print("Deleted item: ",deleted_item)




# Remove an item by value

print("*****Remove Fiat from cars list***********")

cars.remove("Fiat")

print(cars)



 

