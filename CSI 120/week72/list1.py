# Ask user to enter the total number of items
total_items = int(input("Enter total number of items: "))

# Initialize an empty list
cars = []

# Loop to get items from the user and add them to the list
for i in range(total_items):
    item = input(f"Enter Item #{i+1}: ")
    cars.append(item)

# Print the initial list
print("Initial List:", cars)

# Ask the user which item to remove
item_to_remove = input("Which item do you want to remove? ")

# Remove the specified item from the list
cars = [car for car in cars if car != item_to_remove]

# Print the final list
print("Final List:", cars)





