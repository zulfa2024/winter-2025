#accept the user input

choice = "y"

while choice.lower() == "y":
    customer_name = input("Enter the first name: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter how many purchased: "))
    price = int(input("Enter the price per unit: "))
    total_amount = (quantity * price)
    
    print(f"{customer_name} has purchased {quantity}{product_name}'s for ${total_amount}.")
    choice = input("Do you want to continue? (y/n): ")
print("Thank you for shopping!")
    