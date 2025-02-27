# Initial list of cars
cars = ['Audi', 'Fiat', 'Audi']

# Item to remove
item_to_remove = 'Audi'

# Remove all occurrences of the item
cars = [car for car in cars if car != item_to_remove]

# Final list
print("Final List:", cars)
