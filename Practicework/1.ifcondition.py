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
   print("Zero")                    '''                 #Enter the number: 78
                                                    #positive number'''
#even and add
num = int(input("Enter the number: "))
if num%2 == 0:
   print(f'{num} is even number')                  #Enter the number: 69 
else:                                               # 69 is odd number
   print(f'{num} is odd number')                    #Enter the number: 0
                                                    #0 is even number


#Leap year
'''year= int(input("Enter the year: "))
if year%400==0 and year%100!=0:
   print(f'{year} is leap year')
else:
   print(f'{year} is not leap year')            #Enter the number: 2000
                                                    #2000 is even number
                                                    #Enter the year: 679
                                                   #679 is not leap year  '''



                                                      

    