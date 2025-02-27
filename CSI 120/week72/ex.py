
import os
# Initialize the list
cars = ['Audi', 'Fiat', 'Audi']

# Print the initial list
print("Initial list of cars:", cars)

# Remove all instances of 'Audi' from the list
print("*****Remove all instances of 'Audi' from cars list***********")
while "Audi" in cars:
    cars.remove("Audi")

# Print the final list
print(cars)
