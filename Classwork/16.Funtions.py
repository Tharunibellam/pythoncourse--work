# Function with no parameters
#return=the value that is returned by the function=will stop there
def say_hello():
    print("Hello!")

# Function with parameters and return value
def add(a, b):
    return a + b

# Function with a default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Function to find the square of a number
def square(x):
    return x * x

# Example usage
say_hello()                       #Hello!
print(add(3, 5))                  #8
greet("Alice")                    #Hello, Alice!
print(square(4))                  #16

#Types of Functions
#Built-in Functions
print(len("Hello"))               #5
print(max([1, 2, 3]))             #3
print(min([1, 2, 3]))             #1
print(sorted([3, 1, 4, 2]))       #[1, 2, 3, 4]

# User_Defined Funtion
def multiply(x, y):
    return x * y
print(multiply(3, 4))             #12

#Function Arguments
#1.Positional Arguments
'''
def greet(name, age):
    print(f"Hi, I am {name}")
    print(f"My age is {age}")

greet("Alice", 30)  '''                               #Hi, I am Alice
                                                      #My age is 30
#example 
'''
data=('abc@gmail','abc@123')
def login(mail,password,username="Hello"):
    if mail == data[0] and password == data[1]:
        print(f"{username} - login successful")
    else:
        print(f"{username} - Invalid login")
username=input("Enter the username: ")
mail=input("Enterthe mail: ")
password=input("Enter the password: ")

login(mail,password,username)                  #Enter the username: hdguf
    '''                                        #Enterthe mail: fjhwuf
                                               #Enter the password: dje
                                               #hdguf - Invalid login
#2.Keyword Arguments
def greet(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

greet(name="Priya", age=28)                 #Name: Priya
greet(age=28, name="Priya")                 #Age: 28

#Default Arguments  
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")                    # Prints "Hello, Alice!"
greet("Bob", message="Good day")  # Prints "Good day, Bob!"

#1. *args — Arbitrary Positional Arguments
def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4, 5))  # → 15
print(add())               # → 0 (empty)

#**kwargs — Arbitrary Keyword Arguments
def user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")
#3. Combining *args and **kwargs
def mixed(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

mixed(10, 20, 30, name="Bob", country="India")

#Scope of variables
#1. Local Scope
def greet():
    message = "Hello"
    print(message)

greet()            # → Hello
# print(message)   # NameError: message is not defined

#2. Global Scope (G)
x = 10

def update():
    global x
    x = 20

update()
print(x)         # → 20
#3. Enclosing/Nonlocal Scope (E)=nonlocal
def outer():
    msg = "Hi"
    def inner():
        nonlocal msg
        msg = "Hello"
    inner()
    print(msg)    # → Hello
outer()
#4. Built-in Scope (B)
print(len("Python"))  # uses built-in len()

len = 5
print(len("test"))    # TypeError! We've shadowed the built-in len



#Full LEGB Example
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("inner says:", x)
    inner()
    print("outer says:", x)

outer()
print("module says:", x)





















































#Recursive Functions 
def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
s="python program"
display(s,0)

#reverse
def display(s,ind):
    if ind==-1:
        return
    print(s,[ind],end='')
    display(s,ind-1)

s="python is fun"
display(s,len(s)-1)

#type 2 reverese
def display(s,ind):
    if ind==-1:
        return
    print("After:",[ind],end='')
    display("After:",ind-1)

s="python is fun"
display(s,len(s)-1)

#sum of digits with out recuring
n = int(input("Enter the number: "))
sumofdigit = 0
while n > 0:
    sumofdigit += (n % 10)
    n = n // 10
print(sumofdigit)

#with recurtion
def sumofdigits(n):
    if n>0:
        return 0
        sumofdigit=(n%10)+sumofdigit(n//10)
        return 
        
n=int(input("Enter the digits: "))
      
#lambda funtions
#Even or Odd
def evenorodd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
evenorodd(12)
evenorodd(13)
#lambda function for even or odd
evenorodd_lambda= lambda n: "Even" if n%2==0 else "Odd"
print("evenorodd_lambda:",evenorodd_lambda(5))
print("evenorodd_lambda:",evenorodd_lambda(52))

#Square of a number
def square(n):
    return(n*n)
square(3)
square(5)
#lamdba funtion for square
squares_lambda= lambda n: n*n
print("Squares_lambda:",squares_lambda(5))
print("squares_lambda:",squares_lambda(52))


#map in funtions=
def sqa(l):
    for i in  range(len(l)):
        l[i]**=2
sqa([1,2,3,4,5])
sqa([4,5,6,7])

#map funtion
squl_lambda= list(map(lambda i:i**2, [1,2,3,4,5]))
print("squl_lambda",squl_lambda)
v='aeiou'
squl_lambda= list(map(lambda i:'*' if i  in v else i,'python'))
print("squl_lambda",''.join(squl_lambda))

s=sorted([1, 3], [2, 1], [4, 5])(s,key=lambda i:i[1])
print(s)
s=sorted([1, 3], [2, 1], [4, 5])(s,key=lambda i:i[-1])
print(s)
l=[[23,34,56],[21,56,89,30],[78,90,54,35],[43,67,3,17]]  
s=sorted(l,key=lambda i: i[0])
print(s)

#filter funtion=if the condition is true then it will return the value