#Nested Loops
#Syntax of Nested Loops



'''
#Pattern Problems Using Nested Loops
#1. Square Pattern
n = 5 # Change this for different sizes
for i in range(n):
  for j in range(n):
   print('*', end=' ')
  print()                                  # * * * * * 
                                           # * * * * *
                                           # * * * * * 
                                           # * * * * *
                                           # * * * * *      


#Q1
for row in range(3):
    for col in range(5):
        print(col,end=' ')
    print()

#Q1
for row in range(5):
    for col in range(5):
        print(row,end=' ')
    print()

#Q1
for row in range(8):
    for col in range(5):
        print('*',end=' ')
    print()

#Q1
for row in range(7):
    for col in range(row+1):
        print(row,end=' ')
    print()

for row in range(17):
    for col in range(row+1):
        print('*',end=' ')
    print()


for row in range(7):
    for col in range(col-1):
        print(col,end=' ')
    print()

n=int(input("Enter the  size: "))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()

n=int(input("Enter the  size: "))
for row in range(n):
    for spa in range(n-row-1):
        print('',end='')
    for col in range(n-row):
        print('*',end=' ')
    print()


n=int(input("Enter the size: "))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for k in range(n-1):
        print('*',end=' ')
    print()
    n-=1
#Q11
n=int(input("Enter the size: "))
for row in range(n):
   for spc in range(row):
      print(' ',end='')
   for col in range(n-row):
       print("*",end='')
   print()
#type2 above one
for row in range(n):
   print(' '*row,end='')
   print("*"*(n-row),end='')
   print()
#type2 above one
n=int(input("enter the size: "))
for row in range(n):
   if row<=n//2:
      print('*'*(row+1),end='')
   else:
      print('*'*(n-row),end='')
   print()

#Q12
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
          print("*",end='')
        else:
           print(" ",end='')
   print()
#
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 or col==n//2:
          print("*",end='')
        else:
           print(" ",end='')
   print()
#Z pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
          print("*",end='')
        else:
           print(" ",end='')
   print()
#X pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
        if row==col or row+col==n-1  :
          print("*",end='')
        else:
           print(" ",end='')
   print()

#I pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      if row==0 or row==n-1 or col==n//2:
         print("*",end='')
      else:
         print(" ",end='')
   print()

#H pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      if row==n//2 or col==0 or col==n-1:
         print("*",end='')
      else:
         print(" ",end='')
   print()
#S pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      if row==0 or row==n-1 or row==n//2 or (col==0 and row<=n//2) or (col==n-1 and row>=n//2):
         print("*",end='')
      else:
         print(" ",end='')
   print() 

#A pattern

n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      if row==0 or row==n//2  or col==0 or col==0 or col==n-1:
         print("*",end='')
      else:
         print(" ",end='')
   print() 

#V pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      if col==n-1  or row==n//2 or (col==0 and row<=n//2) or (row-col==n//2 and row>=n//2) :
         print("*",end='')
      else:
         print(" ",end='')
   print()

#K pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      if row==0 or row==n-1 or row==n//2 or (col==0 and row<=n//2) or (col==n-1 and row>=n//2):
         print("*",end='')
      else:
         print(" ",end='')
   print()

#T pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      if row==0 or col==n//2 :
         print("*",end='')
      else:
         print(" ",end='')
   print()
#R pattern
n=int(input("Enter the size: "))
for i in range(n):
   for j in range(n):
      if i==0 or j==0:
         print("*",end='')
      else:
         print("",end='')
   print()

#U pattern 
n=int(input("Enter the size: "))
for i in range(n):
   for j in range(n):
      if j==0 or j==n-1 or i==n-1: 
         print("*",end='')
      else:
         print(" ",end='')
   print()
#N pattern
n=int(input("Enter the size: "))
for i in range(n):
   for j in range(n):
      if j==0 or i== or j==n-1:
         print("*",end='')
      else:
         print("",end='')
   print()
#X pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
        if row==col or row<=n//2 or row+col==n-1 and row<=n//2 :
          print("*",end='')
        else:
           print(" ",end='')
   print() '''
#M pattern
n=int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
        if col==0 or col==n-1 or row==n//2:
          print("*",end='')
        else:
           print(" ",end='')
   print()   