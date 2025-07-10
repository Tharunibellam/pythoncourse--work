#Output Formatting
#Understanding the print() Function in Python

#What is print()?
#print(object, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#Basic Examples of print()
#a) Printing Text
print("Welcome to Python Programming!")                      #Welcome to Python Programming!
print("Python is powerful.")                                 #Python is powerful.
print()                                                      #nothing will be print becuase it is an empty

#b) Printing Multiple Items
firstname = "Ram"
lastname = "sai"
course = "python"
age = 21
print("fullname:",firstname,lastname,"course:", course, "age:", age)                #fullname: Ram sai course: python age: 21

#c) Using sep to Change the Separator
print("2024", "01", "12", sep="/")                                          #2024/01/12
print("Mr","vilok", "chowdhary", sep=".")                                   #Mr.vilok.chowdhary
print("Red", "Green", "Blue", sep="-")                                      #Red-Green-Blue

#d) Using end to Control Line Endings
print("Python is", end=" ")
print("awesome!")                                           #Python is awesome!



print("Loading", end="...")
print(" Done!")                                             #Loading... Done!

print("Good", end=" 😊 ")
print("Morning!")                                           #Good 😊 Morning!

#Printing Special Characters
#● New Line (\n):
print("values \nkeys")                                #values                                   
                                                      #keys
print("goodmorning \nevening")                        #goodmorning
                                                      #evening


#● Tab (\t):
print("Name:\tRam")                                 #Name:   Ram
print("cource:\tDS")                                #cource: DS
print("batch:\t15")                                 #batch:  15

#Output Formatting
#1Using Commas (Simple Print Method)
#This is the most basic way to print multiple items. When you separate items with commas in the print() function, Python adds a space between them automatically.
name = "sairam"
age = 23
city = "andhrapradesh"
print("Name:", name, "Age:", age, "City:", city)                    #Name:   Ram cource: DS batch:  15
                                                                     #Name: sairam Age: 23 City: andhrapradesh
#2️.Using Modulo Operator (% Formatting)
#This is an older method, similar to C-style formatting. You use % followed by format specifiers like %s (string), %d (integer), %f (float), etc.
name = "vindhya"
age = 3
city = "andhrapradesh"
marks = 98.9
print(f"name: %s | age: %d  | city:%s | marks: %.2f" % (name,age,city,marks))            #name: vindhya | age: 3  | city:andhrapradesh | marks: 98.90  

#3.Using f-strings (Formatted String Literals) — Python 3.6+
#This is the most modern and recommended method. Add an f before the string and use curly braces {} to insert variables directly.
name = "vindhya"
age = 3
city = "andhrapradesh"
marks = 98.9
print(f"Name: {name} | age: {age} | city: {city} | marks: {marks}")              #Name: vindhya | age: 3 | city: andhrapradesh | marks: 98.9

#4️.Using str.format() Method
#This method works in both Python 2 and 3. You use {} as placeholders and call .format() with the variables you want to insert.
Name = "vindhya"
Age = 3
City = "andhrapradesh"
Marks = 98.9
print("Name: {} | Age: {} |City: {} | Marks: {:.1f}".format(Name, Age,City,Marks))                 #Name: vindhya | Age: 3 |City: andhrapradesh | Marks: 98.9
