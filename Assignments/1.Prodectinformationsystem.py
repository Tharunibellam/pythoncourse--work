#Product Information System Using Different Data Types and Formatting Methods
#Task 1: Take prodect 
#online appa name

Foodapp_name = input("Enter the app name: ")               #Enter the app name: Magicpin 

#1.Fooditem ID in magicpin
Food_ID = int(input("Enter prodect ID: "))                 #Enter prodect ID: 273

#2.food name
Food_Name = input("Enter product name: ")                  #Enter product name: Pizza  

#price(float)
price = float(input("Enter price: "))                      #Enter price: 399.10

#categories(list)
categories_input = input("Enter categories (comma-separated): ")
categories = [category.strip() for category in categories_input.split(',')]        #Enter categories (comma-separated): Chessse tomato pizza,Jain pizza,Paneer delux pizza,Special pizza

#stock details (tuple)
available_stock = int(input("Enter available stock: "))                             #Enter available stock: 23
sold_stock = int(input("Enter sold stock: "))                                       #Enter sold stock: 45
stock_details= (available_stock, sold_stock)

#Discount percentage 
discount_percentage = float(input("Enter discount percentage: "))                   #Enter discount percentage: 19.28

#food review and taste rating.
review = input("Enter Product Review: ")                                            #Enter Product Review: Delicious crust and  cheesy
taste_rating = float(input("Enter Taste Rating (out of 5): "))                      #Enter Taste Rating (out of 5): 4.1

#Restaurant Details(dict)
Restaurant_details = {
    "Name": input("Enter restaurant name: "),                                #Enter restaurant name: Pizza Hub
    "Location": input("Enter restaurant location: "),                        #Enter restaurant location:  Hyderabad,secunderabed,Telangana,F.B Nagar,No.16,Circle,old Alwal,500010
    "Rating": float(input("Enter restaurant rating (out of 5): "))           #Enter restaurant rating (out of 5): 4.1


}
#restaurant_timings = int(input("enter time: "))

#supplier details(dict)
Supplier_details = {
    "Name": input("Enter supplier name: "),                             #Enter supplier name: Sudheer
    "Contact": input("Enter supplier contact number: "),                #Enter supplier contact number: 987654321
    "Location": input("Enter supplier location: ")                      #Enter supplier location::3-4-214/E Beside bank of india,kachiguda,Hyderabad

}
#time to reached the custermer

print("\n--- food details ---\n")

#1.using comma separation (sep=',')
print("Foodappname, Id, Name, price:", Foodapp_name, Food_ID, Food_Name, price)
#2.Using Percentage Formatting (% operator)
print("Food discount:%.2f%%" % discount_percentage)
#3.Using f-strings (f"")
print(f"Foodappname: {Foodapp_name}")                                      
print(f"Food Name: {Food_Name}")                                            
print(f"price: ₹{price:.2f} ")                                              
print(f"Discount: {discount_percentage}%)")
print(f"Stock Avilable: {stock_details[0]} units")
print("categories:", categories)
print("review:",review)
print("taste rating:", taste_rating, "/5")
print("Restaurant details:", Restaurant_details)
print("Supplier details:", Supplier_details)




#--- food details ---



'''Foodappname, Id, Name, price: Magicpin 273 Pizza 399.1
Food discount:19.28%
Foodappname: Magicpin
Food Name: Pizza
price: ₹399.10
Discount: 19.28%)
Stock Avilable: 23 units
categories: ["['Chessse tomato pizza'", "'Jain pizza'", "'Paneer delux pizza'", "'Special pizza']"]
review: Delicious crust and  cheesy
taste rating: 4.1 /5
Restaurant details: {'Name': 'Pizza Hub', 'Location': ' Hyderabad,secunderabed,Telangana,F.B Nagar,No.16,Circle,old Alwal,500010', 'Rating': 4.1}  
Supplier details: {'Name': 'Sudheer', 'Contact': '987654321', 'Location': '3-4-214/E Beside bank of india,kachiguda,Hyderabad'}'''