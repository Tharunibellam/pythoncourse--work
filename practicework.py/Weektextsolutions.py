#Python Weekly Test - 1
#Q1.The Birthday Format Fixer (String & Type Conversion)
#date,month,year=input().split('-')
#print(f'{year}/{month}/{date}')                    
'''Input: 17-07-2025
Output: 2025/07/17
Input: 01-01-2000
Output: 2000/01/01
'''

#Q2.The Even Odd Game (Conditional Statement)
'''
n=int(input())
if n%2==0:
    print("Even Winner")
else:
    print("Odd Winner")

#output:Input: 22
Output: Even Winner
Input: 35
Output: Odd Winner
'''


#Q3. Vowel Replacer Bot (String Methods)
#s=input().lower()
#print(s.translate(str.maketrans('aeiou','*****')))
'''
Input: hello world
Output: h*ll* w*rld
Input: python is fun
Output: pyth*n *s f*n
'''
#Q4.Shopping Cart Analyzer (List Operations)
'''
l=list(map(float,input().split()))
print(sum(l))
print(max(l))
#Python

Python

Python
Test Cases

Input: 10.5 20.0 5.5
Output:
36.0
20.0
Input: 100.0 50.0
Output:
150.0
100.0
'''


#Q5.Secure Login System (Tuple & Conditional)
'''
credentials = ("admin", "python123")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
    print("Login Successful")
else:
    print("Access Denied")

Input:
admin
python123
Output: Login Successful
Input:
admin
wrongpass
Output: Access Denied
'''
#Q6.Remove Duplicates from Set (Set Operations)
'''
names=set(input().split(','))
print(sorted(names))
Input: Ravi,Asha,Asha,John
Output: ['Asha', 'John', 'Ravi']
Input: Meena,Arun,Arun,Ravi
Output: ['Arun', 'Meena', 'Ravi']
'''
##Q8.Reverse My Words (String Slicing)
'''
sen=input().split()
for i in sen:
    print(i[::-1],end=' ')

Input: hello world
Output: olleh dlrow
Input: python is fun
Output: nohtyp si nuf
'''

'''
l=list(map(int,input().split()))
while (0 in l):
    l.remove(0)
print(l)
'''
#Q9.Clean My List (List and Type Conversion)
'''
l=list(map(int,input().split()))
res=[]
for i in l:
    if i!=0:
        res.append(i)
print(res) 

Input: 10 0 5 0 3
Output: [10, 5, 3]
Input: 0 0 1
Output: [1]
'''
#Q10.The Frequency Counter (Dictionary + String)
'''
line=input()
data={}
for i in line:
    if i not in data and i!=' ':
        data[i]=line.count(i)
print(data)

Input: hello world
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd':
1}
Input: a b a
Output: {'a': 2, 'b': 1}


'''
#Q7.Student Marks Record (Dictionary Operations)
'''
n=int(input())
data={}
max_val=0
res_name=''
for _ in range(n):
    name,marks=input().split()
    marks=int(marks)
    if marks>max_val:
        max_val=marks
        res_name=name
        
    data[name]=marks

print(data)
print(res_name)

Input:
3
Ravi 85
Anu 90
Sita 88
Output: Anu
Input:
2
Rahul 70
Meena 75
Output: Meena
'''
#Weekly Assignment = 2
#Q1=Automated salary tax calculator
'''
salary = int(input("Enter the salary: "))
if salary <= 250000:
    print("No Tax")
elif 250000 <= salary <= 500000:
    print(salary * 0.05)
elif 500000 <= salary <= 1000000:
    print(salary * 0.2)
elif salary >= 1000000:
    print(salary * 0.3)           '''                                                   #Enter the salary: 10000000000
                                                                                        #3000000000.0
#Q2=Movie Tickets pricing system
'''
n=int(input())
total_price=0
for i in range(n):
    age=int(input())
    if age<=5:
      continue
    elif 5<=age<=18:
      total_price+=100
    elif 19<=age<=60:
      total_price+=150
    elif age>=60:
      total_price+=120 
                                #3 7 17 35 65
print(total_price)     '''         #output=370

#Q3=Electricity Bill Generator
'''
units = int(input())
if units <= 100:
    print(units*1.5)
elif 101 <= units <= 200:
    bill=(100*1.5)+(units-100)*2.5
    print(bill)
elif 201 <= units <= 500:
    bill=(100*1.5)+(100*2.5)+(units-200)*4
    print(bill)
elif units >= 500:
    bill=(100*1.5)+(100*2.5)+(100*4)+(units-500)*6
    print(bill)                '''                               #250
                                                                 #600.0
 

#Q4=Car packing Fee Calculator
'''
hours = int(input()) 
if hours <= 2:
    print(30)
elif 2<hours<24:
    print(30+(hours-2)*10) 
elif  hours==24:
    print(200)               '''                        #18
                                                        #190
#Q5.Prodect Inventory checker(Nested conditionals)
'''
product = input()
quantity = int(input())
if quantity<0:
    print(f"{product}:out of stock")
elif 1 <= quantity <= 10:
    print(f"{product}:low stock")
elif 11 <= quantity <= 50:
    print(f"{product}: in stock")
elif quantity > 50:
    print(f"{product}: Overstocked")                    #mouse
                                    '''                 #67
#Q6.pattern
''' 
n = int(input())
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ') 
    print()                                                   #mouse: Overstocked
#output:4
0 1 0 1 
1 0 1 0
0 1 0 1
1 0 1 0'''
#Q7.Gym subscription Billing(menu Driven program)
'''
while True:
    print("""1.Monthly - $500
2.Quarterly - $1300
3.Yearly - $5000
0.Exit
""")
    ch=int(input())
    people=int(input())
    if ch==0:
        break
    if ch==1:
     print(500*people)
    elif ch==2:
      print(1300*people)
    elif ch == 3:
       print(5000*people)
    else:
       print("Invalid choice")

#output:1.Monthly - $500
2.Quarterly - $1300
3.Yearly - $5000
0.Exit

2 
3
3900
1.Monthly - $500
2.Quarterly - $1300
3.Yearly - $5000
0.Exit

'''
#Q8.Billing bot-apply discount based on amount
'''
amount=float(input())
discount_acc=0
if 0<amount<=990:
    pass
elif 1000< amount<=4999:
    discount_acc=amount*0.05
elif 5000<amount<=9999:
    discount_acc=amount*0.1
elif amount>10000:
    discount_acc=amount*0.15
print(amount-discount_acc)                       #12000
       '''                                          #10200.0
#Q9.ATM PIN verification with Blocking Logic
'''
stored_pin=9876
for i in range(3):
    pin= int(input())
    if pin==stored_pin:
        print("Acees Granted")
        break
else:
    print("Atm Blocked.try agin later")

#output:7654
6545
5545
Atm Blocked.try agin later
'''  
#Q10.Bus Booking system
'''
total_seat=int(input())
booked_seats=input().split()
print(f'Total Seats: {total_seat}')
print(f'Booked: {len(booked_seats)}')
print(f'Available: {total_seat-len(booked_seats)}')

#output:55
34 23 12 3 2 1 5 7 9 20 21 45 6
Total Seats: 55
Booked: 13
Available: 42
'''






