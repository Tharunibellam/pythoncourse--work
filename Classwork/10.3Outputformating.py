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




#● Tab (\t):

