import os
os.system("cls")
#Enter total number of items: 3  
#Enter Item #1: Audi  
#Enter Item #2: Fiat  
#Enter Item #3: Audi  
cars: ['Audi', 'Fiat', 'Audi']  
#Which item do you want to remove? Audi  
#Final List: ['Fiat']  
# Initialize the list
cars = ['Audi', 'Fiat', 'Audi']

# Print the initial list
print("Initial list of cars:", cars)

# Remove 'Audi' from the list
print("*****Remove all instances of 'Audi' from cars list***********")
cars.remove("Audi")
print(cars) 


