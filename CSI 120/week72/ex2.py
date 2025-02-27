import os
# add cars in car list variave: "Audi, Fiat,tesla,honda,toyota,yyyy,ghy,hcgds,lohh,hkhks"
# cars: [] Remove all occurances of a particular item ....Audi
#Enter total no of items:3
#Enter Item #1: "Audi"
#Enter Item #2: "Fiat"
#Enter Item #2: "Audi"
#Enter Item #3: "tesla"
#Enter Item #4: "honda"
#Enter Item #5: "Toyota"
#Enter Item #6: "yyyy"
#Enter Item #7: "ghy"
#Enter Item #8: "hcgds"
#Enter Item #9: "lohh"
#Enter Item #10: "hkhks"
#cars: [Audi, Fiat,tesla,honda,toyota,yyyy,ghy,hcgds,lohh,hkhks]

os.system("cls")
cars = ["Audi", "Fiat", "tesla", "honda", "toyota", "yyyy", "ghy", "hcgds", "lohh", "hkhks"]
total_items = int(input("Enter total no of items: "))
#append items in list: tesla"
cars.append("tesla")


#remove all occurances of a particular item

#Which item do you want to remove: Audi
# Final List: [Fiat]
