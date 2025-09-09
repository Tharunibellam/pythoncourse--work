#OOP (Object-Oriented Programming) is a way of writing code by grouping data and functions together into classes and objects.
#Class = Blueprint (like a design of a car 🚗)
#Object = Real thing made from blueprint (like your car)
'''Class → Blueprint of an object.

Object → Instance of a class.

Attributes → Variables inside a class.

Methods → Functions inside a class.

Inheritance → A class can use features of another class.

Encapsulation → Hiding details, exposing only what is needed.

Polymorphism → Same function name, different behaviors.'''

#OOPS Example in python
# Class (Blueprint)
class BankAccount:
    # Constructor (runs when object is created)
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance = {self.balance}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. New Balance = {self.balance}")
        else:
            print("Insufficient balance!")

    # Method to show account info
    def show_info(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


# ------------------------------
# Creating Objects (Real Accounts)
acc1 = BankAccount("Tharuni", 5000)
acc2 = BankAccount("Rahul", 1000)

# Using Methods
acc1.show_info()
acc1.deposit(2000)
acc1.withdraw(3000)

acc2.show_info()
acc2.withdraw(1500)  # Will show insufficient balance
'''Owner: Tharuni, Balance: 5000
Deposited 2000. New Balance = 7000
Withdrew 3000. New Balance = 4000
Owner: Rahul, Balance: 1000
Insufficient balance!'''


from abc import ABC, abstractmethod
class Bankaccount(ABC):
    def deposit(self):
        print("You can deposit amount")
    def Checkbalance(self):
        print("You can check your balance")
    @abstractmethod
    def withdraw(self):
        pass
    def viewhistory(self):
        print("You can check the history")
class CurrentAccount(Bankaccount):
    def withdraw(self):
        print("You can withdraw Extra amount also")
class SavingAccount(Bankaccount):
    def withdraw(self):
        print("You can withdraw amount")

mani=CurrentAccount()
shanmukh=SavingAccount()
mani.Checkbalance()
mani.deposit()
mani.viewhistory()
mani.withdraw()
shanmukh.Checkbalance()
shanmukh.deposit()
shanmukh.viewhistory()
shanmukh.withdraw()

'''You can check your balance
You can deposit amount
You can check the history
You can withdraw Extra amount also
Ypu can check your balance
You can deposit amount
You can check the history
You can withdraw amount'''

#Read mode
#if have no file it show an error 
try:
    file=open('demo.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    read=file.read()
    file.seek(0)
    readlines=file.readlines()
    file.seek(0)
    readline=file.readline()
    print(f"\nFile content using read():\n{read}")
    print(f"\nFile content using readlines():\n{readlines}")
    print(f"\nFile content using readline():\n{readline}")
    file.close(0)
finally:
    print("Rest of the code")

#Write mode
#if we have no file then i tcreat a new file
try:
    file=open('dsda.txt','w')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam')
    file.close()
finally:
    print("Rest of the code")

#append mode 
try:
    file=open('dsda.txt','a')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam\n')
    file.close()
finally:
    print("Rest of the code")

#append + read
try:
    file=open('dsda.txt','a+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code")
'''monday we have exammonday we have exam
monday we have exam

Rest of the code'''
#read+=write + read
try:
    file=open('dsda.txt','r+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code")
'''monday we have exam
nday we have exam
monday we have exam

Rest of the code'''
#write+=read + write
try:
    file=open('dsda.txt','w+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code")
'''monday we have exam

Rest of the code'''
#with open as how to it automatically close it
with open('dsda.txt','r+') as file:
    file.write('\nFile operations')
    file.seek(0)
    print(file.read())

import os
print(os.getcwd())
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')

'''
#rmdir=remove
import os
if os.path.exists('DSDA'):
    os.rmdir('DSDA')
'''
#
import os
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
    os.makedirs('DSDA')

import os
import shutil
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
    os.makedirs('DSDA/1415')
#os.rmdir('DSDA')
shutil.rmtree('DSDA')



import re
res=re.search(r'[0-9]','ds-da-14-15')
print(res.group() if res else "No pattern")

#findall=dirctly gives  
import re
res=re.findall(r'[0-9]{2}','PFS-30  & ds-da-14-15')
print(res)


import re
res=re.findall(r'\s','python pythox psthons  pithin')
print(res)

import re
res=re.findall(r'\w+','python pythox psthons  pithin')
print(res)

import re
res=re.findall(r'p..h.n','python pythox psthons  pithin')
print(res)

#finditer=lasyly evaluates and returns an iterator
import re
res=re.finditer(r'[0-9]{2}','PFS-30  & ds-da-14-15')
for i in res:
    print(i.group(),i.start())

import re
res=re.finditer(r'[0-9]{2,}','PFS-30  & ds-da-14-15')
for i in res:
    print(i.group(),i.start())

#match=only checks from staring start
import re
res=re.fullmatch(r'(aeiou)','aeiou')   #[]=will match if change in pattern  ()=it need to match the pattern
print(res.group() if res else "No pattern")

import re
res=re.fullmatch(r'^[6-9]\d{9}','9876543210')
print(res.group() if res else "No pattern")

import re
res=re.fullmatch(r'DA-..','')
print()

#split()=
import re
res=re.split(r'\s','python pythox pstgoon splleitr')
print(res)

import re
res=re.split(r'[,;"-]','python pythox pstgoon splleitr')
print(res)
#sub
import re 
res=re.sub(r'[aeiouAEIOU]','*0*','pyton is a programming Language')
print(res)              #pyt*0*n *0*s *0* pr*0*gr*0*mm*0*ng L*0*ng*0**0*g*0*

import re
res=re.sub(r'[0-9]','pyton3.7 programming')


fullname=