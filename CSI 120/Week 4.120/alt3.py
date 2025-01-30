#accept customer name , productName , quantity, price from the user and display results in the format:
#customerName, : Rey William #productName, : Laptop
 #quantity, : 2
 #price, : 1000
 #total amount: 2000 (calculated)
 #customer Rey William purchased 2 laptops for $2000
 #do you want to continue?(y/n):y
 #customer Name Shane Williams
 #productName, : keyboard
 #quantity, : 4
 #price, : 40
 #total amount: 160
 #customer Shane Williams purchased 4 keyboards for 160
 #do you want to continue?(y/n):n
def get_customer_details():
    name = input("Customer Name: ")
    product = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    return name, product, quantity, price

def calculate_total_amount(quantity, price):
    return quantity * price

def display_result(name, product, quantity, price, total_amount):
    print(f"Customer Name: {name}")
    print(f"Product Name: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print(f"Total Amount: {total_amount}")
    print(f"Customer {name} purchased {quantity} {product}(s) for ${total_amount}")

# Get customer details
name, product, quantity, price = get_customer_details()

# Calculate total amount
total_amount = calculate_total_amount(quantity, price)

# Display result
display_result(name, product, quantity, price, total_amount)

# Ask if the user wants to continue
continue_entry = input("Do you want to continue? (y/n): ")
if continue_entry.lower() == 'y':
    # Get new customer details
    name, product, quantity, price = get_customer_details()
    total_amount = calculate_total_amount(quantity, price)
    display_result(name, product, quantity, price, total_amount)

 