#List comprehension
'''
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob"]
mixed = [1, "hello", True, 3.5]
'''
'''


#Normal form
n=int(input("Enter the number: "))
l=[]
for i in range(1,n+1):
    l.append(i)
print(l)
#List comprehension form
k=[i for i in range(1,n+1)]                  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(k)
#List comprehension with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [n for n in numbers if n % 2 == 0]
print(evens)                                  #[2, 4, 6, 8]

#set and list comprehention
d=[]
for i in range(10):
    d.append(i*i)
print(d)
#
d=[i*i for i in range(10)]
print(d)    
                         #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'''
'''
s = 'python'
result = []
for i in s:
    result.append(i.upper())
print(result)

s='python'
s=[i.upper() for i in s]
print(s)

j='programming'
v='aeiouAEIOU'
o=[]
for i in j:
    if i in v:
        o.append(i)
print(o)
j='programming'
v='aeiouAEIOU'
o=[i for i in j if i in v]           #['o', 'a', 'i']
print(o)

#Uppercase a list of strings
s=["python","Java", "Datascience","Machine Learning"]
upper_case=[i.upper() for i in s]
print(upper_case)                    #['PYTHON', 'JAVA', 'DATASCIENCE', 'MACHINE LEARNING']

#Apply 10% discount
salary = [10200, 12300, 15000, 16000, 18000]
discount=[salary * 0.9 for salary in salary]
print(discount)                                          #[9180.0, 11070.0, 13500.0, 14400.0, 16200.0]

#Stock status (boolean)
stock = [True,  False, True, False, 0, 1]
stock_available = [i for i, stock in enumerate(stock) if stock]
print(stock_available)                                   #[0, 2, 5]

#List of dictionaries
products_data = [
{"name": "Laptop", "price": 1000, "stock": 3},
{"name": "Phone", "price": 800, "stock": 0},
{"name": "Tablet", "price": 450, "stock": 5}
]
available_names = [p["name"] for p in products_data if p["stock"] > 0]
print(available_names)                # Output: ['Laptop', 'Tablet']
discounted_products = [{p["name"]: p["price"] * 0.9} for p in products_data if p["stock"] > 0]
print(discounted_products)                   #[{'Laptop': 900.0}, {'Tablet': 405.0}]
'''
products_data = [
{"name": "Laptop", "price": 1000, "stock": 3},
{"name": "Phone", "price": 800, "stock": 0},
{"name": "Tablet", "price": 450, "stock": 5}
]
result = [f"{p['name']} - ${p['price'] * 0.9:.2f}" for p in
products_data if p["stock"] > 0]
# ['Laptop - $900.00', 'Tablet - $405.00']

products_colors = [
{"name": "Laptop", "colors": ["Silver", "Black"]},
{"name": "Phone", "colors": ["Gold", "Blue"]}
]
all_colors = [color for product in products_colors for color
in product["colors"]]
# ['Silver', 'Black', 'Gold', 'Blue']