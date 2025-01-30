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
    customer_name = input("Customer Name: ")
    product_name = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price (per unit): "))
    return customer_name, product_name, quantity, price

def calculate_total_amount(quantity, price):
    return quantity * price

def display_result(customer_name, product_name, quantity, price, total_amount):
    print(f"Customer Name: {customer_name}")
    print(f"Product Name: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print(f"Total Amount: {total_amount}")
    print(f"Customer {customer_name} purchased {quantity} {product_name}(s) for ${total_amount}")

def main():
    while True:
        customer_name, product_name, quantity, price = get_customer_details()
        total_amount = calculate_total_amount(quantity, price)
        display_result(customer_name, product_name, quantity, price, total_amount)
        
        continue_entry = input("Do you want to continue? (y/n): ")
        if continue_entry.lower() != 'y':
            break
if __name__ == "__main__":
        main()
        
            




