#1.Arithmetic operators
a=10
b=20
print("Addition(+):",a+b)       # Addition(+): 30
print("Subtraction(-):",a-b)  # Subtraction(-): -10
print("Multication(*):",a*b)  # Multication(*): 200
print("Division(/):",a%b)     # Division(/): 10
print("Floor Division(//):",a//b)  #Floor Division(//): 0
print("Modulus(%):",a%b)          #Modulus(%): 10
print("Exponentiation(**):",a**b) #Exponentiation(**): 100000000000000000000


#2.Comparison opertors

print("Equal to(==):",a==b)   #Equal to(==): False
print("Not Equal to(!=):",a!=b)  #Not Equal to(!=): True
print("Greater than (>):",a>b)   #Greater than (>): False
print("Less than (<):",a<b)     #Less than (<): True
print("Greater than Equal to(>=):",a>=b)  #Greater than Equal to(>=): False
print("Less than or Equal to(<=):",a<=b)  #Less than or Equal to(<=): True

      

#3.Assignment Operators

# Initial value
x = 10
print("Initial x:",x)

x += 5
print("x += 5:",x)  #x += 5: 15

x -= 3
print("x -= 3:",x)  #x -= 3: 12

x *= 2
print("x *= 2:",x)  #x *= 2: 24

x /= 4 
print("x /= 4:",x)   #x /= 4: 6.0

x = 15
x //= 2
print("x //= 2:",x)  #x //= 2: 7

x %= 5
print("x %= 4:",x)   #x %= 4: 2

x **= 3
print("x **= 3:",x)  #x **= 3: 8


#4.Logical operators

x = 10
y = 20
print(x > 5 and y < 30) #True (Both condition are conition) 

print(x > 15 or y < 30)  #True (Least one condition is True)

print(not (x > 5))      #False:(Reverses the True condition)


#5.Membership operators

student = ["name", "email", "brach", "age"]
print("name" in student)     #True (name is in the student)
print("year" not in student)  #True (year is not in student)

#6.Identity operators


a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=[1,2,3,4,5]

b=a
print(a is b)      #True(Both refer to the same)
print(a is c)      #Flase(Both refer to the different objects)
print(b is c)      #Flase(Both refer to the different objects)
print(a is not b)  #Flase
print(b is not c)  #True


