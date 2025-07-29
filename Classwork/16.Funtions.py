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

greet(name="Priya", age=28)
greet(age=28, name="Priya")  

#Default Arguments  





































































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
      


            