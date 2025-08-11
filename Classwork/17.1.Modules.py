#import operator
#import operator as opr
'''
from operators  import *
# from operators 
a=int(input("Enter a: "))
b=int(input("Enter b: "))
op=input("Enter the op(+-/*%**): ")
if op=='+':
    add(a,b)
elif op=='-':
    sub(a,b)
elif op=='/':
    div(a,b)
elif op=='*':
    mul(a,b) 

'''

#ATM

import ATMlogic as atm
atm.Welcome()

if atm.Login():
  while True:
    atm.Menu()
    ch=input("Enter the choice: ").upper()
    if ch=='C':
      atm.Check_balance()  
    elif ch=='D':
      atm.Deposit()
    elif ch=='W':
      atm.Withdraw()
    elif ch=='V':
      atm.View_transaction()
    elif ch=='E':
      print("Thankyou".center(50,'_'))
      break
    else:
      print("Invalid choice")

'''****************Welcome to the ATM****************
Enter the account number: 23456   
Enter the pin: 143  
Login Successful

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: C    

Current Balance: 3428

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: D   
Enter the amount to deposit: 4367
$4367 is successfully desposited

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: 4367
Invalid choice

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: V
---------------Transactions History---------------
Deposited - $4367
----------------End of the history----------------

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: D
Enter the amount to deposit: 367309
$367309 is successfully desposited

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: D63487
Invalid choice

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: C

Current Balance: 375104

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: V    
---------------Transactions History---------------
Deposited - $4367
Deposited - $367309
----------------End of the history----------------

[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit

Enter the choice: E
_____________________Thankyou_____________________'''










































