#Conditional Statements
#In Python, the main types of conditional statements are:
#1.if Statement
#2.if-else Statement
#3.if-elif-else Statement
#4.Nested Conditional Statements


#1.if Statement

'''x = 10
if x > 0:
    print("x is positive")                                  #x is positive

#Checking Amazon Stock Availability
amazon_stock = 20                                       # Number of items in stock
if amazon_stock > 0:
   print("Amazon stock is available!")                  #Amazon stock is available!


#2.if-else Statement

number = int(input("Enter a number: "))

if number >= 0:
    print("The number is positive or zero.")
else:
    print("The number is negative.")                 #Enter a number: 56
                                                    #The number is positive or zero.
#Example1: Check for Password Match python Copy code

password = input("Enter your password: ")

if password == "admin123":
    print("Access granted.")
else:
    print("Access denied.")                           #Enter your password: thara123@
                                                       #Access denied.
#Example2:
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number or zero")                #Enter a number: 13
                                                    #Positive odd number

#Example3:
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")                               #Enter a number: 13
else:                                           #Positive
    print("Negative")                           #Done checking


print("Done checking.")                               




#3. if-elif-else Statement
color = input("Enter traffic light color (red/yellow/green): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")                   #Enter traffic light color (red/yellow/green): green
                                             #Go


#  Day of the Week
day = int(input("Enter a number (1 to 7): "))

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Invalid day number")                    #Enter a number (1 to 7): 5
                                                   #Thursday

#4. Nested Conditional Statements
age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ").lower()

if age >= 18:
    if citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")                                 #Enter your age: 21
else:                                                                           #Are you an Indian citizen? (yes/no): yes
    print("You must be at least 18 years old to vote.")                         #You are eligible to vote.


#example78

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and b + c > a and a + c > b:  # Valid triangle
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")                        
                                                            #Enter side a: 5
    else:                                                   #Enter side b: 6
        print("Scalene triangle")                           #Enter side c: 8
else:                                                       #Scalene triangle
    print("Not a valid triangle")'''


