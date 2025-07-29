#products
'''data = {
    1:{'name':'Rice','price':60},
    2:{'name':'Wheat Flour','price':45},
    3:{'name':'Sugar','price':70},
    4:{'name':'Milk','price':40},
    5:{'name':'Eggs(12 pcs)','price':70},
    6:{'name':'Cooking oli','price':130},
    7:{'name':'Tea Power','price':90},
    8:{'name':'Salt','price':20},
    9:{'name':'Bread','price':30},
    10:{'name':'Soap','price':25}
       
}
for i in data:
    print(f'{i}. {data[i]["name"]} - ${data[i]["price"]}')           #we have taken dic in dic so i data and price
items=list(map(int,input("Enter the product indexes(1 2 3 4): ").split()))
total=0
s=set()
for i in items:
    if i not in s:
        c=items.count(i)
        print(f'{data[i] ["name"]}-{c}*${data[i] ["price"]}=${c*data[i]["price"]}')
        total+=data[i]["price"]*c
        s.add(i)
print(f"Total Bills: {total}")                             #Total Bills: 585        

#type two in above one
total=0
while True:
    product_name=input("Enter the product name(0-Exit): ")
    if product_name=='0':
        print("Thank you")
        break
    price=int(input("Enter the price: "))
    quantity=int(input("Enter the quantity: "))
    total+=price*quantity
print("Total Amount:",total)

#type2
total=0
data={
    'milk':30,
    'bread':50,
    'sugar':45,
    'oil':180
}
print(data)
while True:
    product_name=input("Enter the product name(0-Exit): ")
    if product_name=='0':
        print("Thank you")
        break
    price=int(input("Enter the price: "))
    quantity=int(input("Enter the quantity: "))
    total+=data[product_name]*quantity: 
print("Total Amount:",total)
'''
#Photo Gallery:
'''photo_gallaery = {
    1:"beach.png",
    2:"mountain.jpg",
    3:"party1.jpg",
    4:"selfie.png",
    5:"birthday.png",
    6:"coucer.jpg",
    7:"sunset.png",
    8:"trip1.jpg"
}
for i in photo_gallaery:
    print(f'{i}.{photo_gallaery[i]}')
l=set(map(int,input("Enter the photo_gallaery indexes(1 2 3 4): ").split(',')))   

for i in l:
    print(f"{photo_gallaery[i]}-shared") '''

#output:
'''1.beach.png
2.mountain.jpg
3.party1.jpg
4.selfie.png
5.birthday.png
6.coucer.jpg
7.sunset.png
8.trip1.jpg
Enter the photo_gallaery indexes(1 2 3 4): 1,2,3,4,4,4,5
beach.png-shared
mountain.jpg-shared
party1.jpg-shared
selfie.png-shared
birthday.png-shared
'''
#prime numbers
'''
n=int(input("Enter the number: "))
for j in range(2,n+1):
    c=0
    for i in range(2,j//2+1):
        if j%i==0:
            c+=1
    if c==0:
        print(f'{j}: prime number' )
        '''
#output:
'''Enter the number: 120
2: prime number
3: prime number
5: prime number
7: prime number
11: prime number
13: prime number
17: prime number
19: prime number
23: prime number
29: prime number
31: prime number
37: prime number
41: prime number
43: prime number
47: prime number
53: prime number
59: prime number
61: prime number
67: prime number
71: prime number
73: prime number
79: prime number
83: prime number
89: prime number
97: prime number
101: prime number
103: prime number
107: prime number
109: prime number
113: prime number
'''
#
