# If-else:
'''items=['shoes','smartwatch','phone','laptop','airpods','toycar']
print('Welcome to Amazon store'.center(50,'*'))
searchinput=input("Enter the item:").lower()
if searchinput in items:
    print(f"{searchinput} fouund. Buy now!!!")                                 #output:Enter the item:shoes
else:
    print(f"{searchinput}, is out of stock.we will notify")    '''            #shoes fouund. Buy now!!!
                                                                               #Enter the item:Ac
                                                                               # ac, is out of stock.we will notify


#Weekend Budget plan
'''amount=input(input("Enter hte amont you can spend for weekend: "))
if amount>2000:
   print("Trip to goa")
elif amount>15000:
   print("go for shopping")
elif amount>10000:
   print("clublingg")
elif print>5000:
   print("cafe/Dinner")                                   #
elif amount>2000:
   print("maintancess")
elif amount>500:
   print("go for movie")
elif amount>100:
   print("enjoy in pg")
else:
   print("sleep and watch movie in phone")     '''               #Enter the amount youucan spend for the weekend:800
                                                               #save the money     
                                                               # #output:Enter the amount youucan spend for the weekend:5000
                                                               #go to movie
#Grading System

'''data={
    1:{'name':'lashkmi','attempt_status':False,'python':0,'sql':0,'powerbi':0},
    2:{'name':'sudhakar','attempt_status':True,'python':100,'sql':90,'powerbi':80},
    3:{'name':'chaithanya','attempt_status':True,'python':70,'sql':90,'powerbi':50},
    4:{'name':'vilok','attempt_status':True,'python':30,'sql':100,'powerbi':25},
    5:{'name':'vindhya','attempt_status':True,'python':60,'sql':40,'powerbi':35},
}

stuid=int(input("Enter the student id: "))

if data[stuid]['attempt_status']:
    total=(data[stuid]['python']+data[stuid]['sql']+data[stuid]['powerbi'])/3
    if total>90:
        print(f'Congrats!!!\n{data[stuid]["name"]} got "A" grade')
    elif total>75:
        print(f'Good!!!\n{data[stuid]["name"]} got "B" grade')
    elif total>50:
        print(f'Try it improve!!!\n{data[stuid]["name"]} got "C" grade')               #Enter the student id: 3
    elif total>35:                                                                     #Try it improve!!!
        print(f'Just Passed!!!\n{data[stuid]["name"]} got "D" grade')                  #chaithanya got "C" grade
    else:
        print(f'Better luck next time!!!\n{data[stuid]["name"]} failed')
        
else:
    print(f'{data[stuid]["name"]} is not attempted the exam.')                                                         


#Positive and negitive numbers
number = int(input("Enter the number: "))
if number>0:
   print("positive number")                       #Enter the number: 0
elif number<0:                                    #zero
   print("negitive number")
else: 
   print("Zero")                                   #Enter the number: 78
                                                   #positive number'''
#even and add
'''num = int(input("Enter the number: "))
if num%2 == 0:
   print(f'{num} is even number')                  #Enter the number: 69 
else:                                               # 69 is odd number
   print(f'{num} is odd number')                    #Enter the number: 0
                                                    #0 is even number    '''


#Leap year
'''year= int(input("Enter the year: "))
if year%400==0 and year%100!=0:
   print(f'{year} is leap year')
else:
   print(f'{year} is not leap year')            #Enter the number: 2000
                                                    #2000 is even number
                                                    #Enter the year: 679
                                                   #679 is not leap year  
'''
#positive and negative
'''num = int(input("Enter the num: ))
if num % 2:
   print("positive")
else:
   print("negative") '''

#Divisible by 5
'''num = int(input("Enter the num: "))
if num % 5 == 0:
   print("divisible by num")
else:
   print("not divisible by num")   
   '''

#Divisible by 3 and 7
'''num = int(input("Enter the num: "))
if num % 3 == 0 and num % 7 == 0:
   print("divisible by both 3 and 7 ")
else:
  print("not divisible")  
'''                                                    #Enter the num: 21
                                                       #divisible by both 3 and 7 
#check for leap year
'''
year = int(input("Enter the year: "))
if year % 4 == 0:
    print("leap year")
else:
  print("not a leap year")                        #Enter the year: 2024
'''                                                #leap year
#Check pass or Fail
'''
marks = int(input("Enter the marks: "))
if marks >= 35:
    print("pass")
else:
    print("Fail")                                     #Enter the marks: 40
'''                                                  #pass
#check if number is 3-digit
''' 
num =  int(input("Enter the num: "))
if num>=99:
    print("3-digit number")
else:
    print("not 3-digit num")                              #Enter the num: 123
'''                                                          #3-digit number
#check the character is vowel
'''
letter = input("Enter the letter: ")
char = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' )
if letter in char:
    print("vowel")
else:
    print("not vowel")                                #Enter the letter: E
'''                                                   #vowel
#greatest of two numbers
'''
a , b = 7 , 9
if a > b :
    print(f"{a} is greater")
else:
    print(f"{b} is greater")          '''               #9 is greater
#smaller num
'''
a = 3
b = 8
if a<b:
    print(f"{a} is smaller")
else:
    print(f"{b} is Not smaller")         '''               #3 is smaller
#check if num is zero
'''
number = int(input("Enter the num: "))
if number == 0:
    print("number is zero")
else:
    print("number is not zero")           '''                  #number is zero
#multiple of 10
'''
number = int(input("Enter the number: "))
if number % 10 == 0:
    print("multiple of the 10")
else:
    print("not multiple of the 10")                    #Enter the number: 56
'''                                                    #not multiple of the 10
#if age is eligible to vote(18+)
'''
age = int(input("Enter the age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("not Eligible to vote")                      #Enter the age: 17
'''                                                       #not Eligible to vote
#if number is between 1 to 100
'''
num = int(input("enter the num: "))
if num in range(1,101):
    print("In range")
else:
    print("out of range")                             #enter the num: 79
'''                                                      #In range

#check num is square of another
'''
num , root = 4,2
if root * root == num:
    print(f" {num} is square of {root}")
else:
    print(f"{num} is not square of {{root}}")  '''         # 4 is square of 2
#if two strings are equal
'''
str1 = "apple"
str2 = "apple"
if str1 == str2:
    print("strings are are equal")
else:
    print("strings are not equal")     '''                  #strings are are equal
#Check if a number is prime (basic logic)
'''
n=int(input("Enter the number: "))
n = 7 
if n <= 1:
    print("not a prime numbers")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("prime number")  '''                       #Enter the number: 7
                                                         #prime number
# if number is positive and even
'''
number = int(input("Enter the num: "))
if number > 0 and number % 2 == 0:
    print("positive and even number")
else:
    print("Did not meet criteria")                       #Enter the num: 12
                                     '''                   #positive and even number

#Check if character is uppercase
'''
char = input("Enter the char: ")
if char.isupper():
    print("uppercase letter")
else:
    print("Not a upperase letter")                  #Enter the char: A
    '''                                                #uppercase letter

#Check if temperature is hot (>30°C)
'''
tem = int(input("Enter the temperature: "))
if tem > 30:
    print("It's hot")
else:
    print("It's not hot")                             #Enter the temperature: 35
    '''                                                  #It's hot
#check if a number is a 4-digit even nimber
'''
num = int(input("Enter the num: "))
if 1000 <= num <= 9999 and num % 2 == 0:
    print("4-digit even num")
else: print("not a 4-digit even num")                    #Enter the num: 2468
     '''                                                    #4-digit even num
#Check if a character is a consonant
'''
char = input("Enter the char: ")
if len(char) != 1 or not char.isalpha():
    print("Not a letter")
if char.lower() not in 'aeiou':
    print("Consonant")
else:
    print("Vowel")
'''
#Check if a number is divisible by 2 or 3 but not both
'''
num = int(input("Enter the num: "))
if num % 2 == 0 and num % 3 == 0:
    print("divisible by both 2 and 3")    
elif num % 2 == 0:
        print("divisible by only 2")
elif num % 3 == 0:
        print("divisible by only 3")               #Enter the num: 4
                                                    #divisible by only 2
else:
    print("not divisible by both")                 #Enter the num: 12
'''                                                #divisible by both 2 and 3
#Check if a number is negative and odd
'''
num = int(input("Enter the num: "))
if num < 0 and num % 2 != 0 :
    print("negive and odd num")
else:
    print("not negitive and odd num")             #Enter the num: -5
       '''                                            #negive and odd num
#Check if a string starts with a vowel   
'''
sen = input("Enter the str: ")
if sen.lower().startswith(('a', 'e', 'i', 'o', 'u')):
     print("starts with a vowel")
else:
    print("does not start with a vowel")                  
    '''                                                   #Input: "apple"
                                                     #Output: Starts with a vowel
#Check if three sides form a valid triangle
'''
a, b, c = 3, 4, 6 
if  (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")
else:
    print("invalid Triangle")       #Valid Triangle              
'''
#Find the greatest among three numbers
'''
num1 = 12
num2 = 45
num3 = 30
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else: 
    greatest = num3
print(f'{greatest} is the greatest')         
                                   '''           #Input: 12, 45, 30
#Practice class work
                                             #Output: 45 is the greatest




