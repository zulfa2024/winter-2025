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
 
 # choice  = "y"
 
while choice == "y": 
    customerName = input("Customer Name: ")
    productName = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    totalAmount = quantity * price
    print(f"{customerName}, : {productName}")
    print(f"quantity, : {quantity}")
    print(f"price, : {price}")
    print(f"total amount: {totalAmount}")
    print(f"{customerName} purchased {quantity} {productName} for ${totalAmount}")
    print("do you want to continue?(y/n):")
    
    