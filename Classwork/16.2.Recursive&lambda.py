#Recursive Functions 
'''def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
s="python program"
display(s,0)'''

#output:
'''
p
y
t
h
o
n
 
p
r
o
g
r
a
m
'''
'''
#def display(s,ind):
    if ind<0:
      return
    print(s[ind])
    display(s,ind-1)
s="python program"
display(s,17)  
#def display(s,c):
    if c==len(s)+1:
        return
    print(s[:c])
    display(s,c+1)
s='abcdefgh'
display(s,1) 

#output

ab
abc
abcd
abcde
abcdef
abcdefg
abcdefgh

#[]=seq=str/tuple/dict/list/set/num
#strings
def display(s,c):
  if c==len(s)+1:
    return
  print(s[:c],"c=",c)
  display(s,c+1)

s='abcdefgh'
display(s,1)
#output:
# a c= 1
ab c= 2
abc c= 3
abcd c= 4
abcde c= 5
abcdef c= 6
abcdefg c= 7
abcdefgh c= 8

def display(s,ind):
    if ind==len(s)-sub+1:
        return
    print(s[ind:ind+sub],ind)
    display(s,ind+1)
s='abcdefgh'
sub=3
display(s,0) 
#output:abc 0
bcd 1
cde 2
def 3
efg 4
fgh 5

#list
def display(l,ind):
  if ind==len(l):
    return
  print(l[ind])
  display(l,ind+1)
l=[1,2,3,4,5,6,7,8,9,10]
display(l,0)
1
2
3
4
5
6
7
8
9
10

def display(l,ind):
  if ind<0:
    return
  print(l[ind])
  display(l,ind-1)

l=[1,2,3,4,5,6,7,8,9,10,45,23,12,45,56,89]
display(l,len(l)-1)
#output:
# 89
56
45
12
23
45
10
9
8
7
6
5
4
3
2
1
#tuple
def display(t,ind):
   if ind==len(t):
       return
   print(t[ind])
   display(t,ind+1)

t=(56,98,23,54,90,12,23,41)   
display(t,0)
#output:
# 56
98
23
54
90
12
23
41
#dic
def display(l,ind):
    if ind==len(l):
        return
    print(l[ind],d[l[ind]])

d={'name':'xyz','age':60,'gender':'M','mail':'xyz@gmail.com','phoneno':234567890}
display
    
  
#example
def numbers(n):
    if n==0:
        return n
    return n+numbers(n-1)
print(numbers(10))              #55                

#Example
def product(n):
    if n==1:
        return n
    return n*product(n-1)
print(product(10))                #3628800

#reverse

def display(s,ind):
    if ind==-1:
        return
    print(s,[ind],end='')
    display(s,ind-1)

s="python is fun"
display(s,len(s)-1)
#n [12]u [11]f [10]  [9]s [8]i [7]  [6]n [5]o [4]h [3]t [2]y [1]p [0]
#type 2 reverese
def display(s,ind):
    if ind==-1:
        return
    print("After:",[ind],end='')
    display("After:",ind-1)

s="python is fun"
display(s,len(s)-1)
   
#sum of digits with out recuring
n = int(input("Enter the number: "))
sumofdigit = 0
while n > 0:
    sumofdigit += (n % 10)
    n = n // 10
print(sumofdigit)

#with recurtion
def sumofdigits(n):
    if n>0:
        return 0
        sumofdigit=(n%10)+sumofdigit(n//10)
        return 
        
n=int(input("Enter the digits: "))

def update(n):
    if n==0:
        return 0
    print("Before:",n)
    update(n-1)
    print("After :",(n))
n=int(input())
print(update(n))

#output:
Before: 9
Before: 8
Before: 7
Before: 6
Before: 5
Before: 4
Before: 3
Before: 2
Before: 1
After : 1
After : 2
After : 3
After : 4
After : 5
After : 6
After : 7
After : 8
After : 9
None

#Q3
def sumofnums(n):
    if n==0:
        return 0
    return n+sumofnums(n-1)
sumofnums(12)
print(sumofnums(12))                  #output: 78

#Q4
def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)
print(factorial(8))           #40320
print(factorial(10))          #3628800

#Q5
def reverse(s,ind):
    if ind==len(s):
        return
    reverse(s,ind+1)
    print(s[ind],end='')
s="python programming"
reverse(s,0)
#output: gnimmargorp nohtyp

#q6
def fibonacci_num(n):
     if n==0:
     return 
    

#Q7
def sumofdigit(n):
    if n==0:
        return 0
    return (n%10) + sumofdigit(n//10)
sumofdigit(7842708142)
print(sumofdigit(7842708142))   #output: 43

#Q8
def countofnum(n):
    if n==0:
        return 0
    return 1 + countofnum(n//10)
n=int(input())
print(countofnum(n))         #6839026450265341894=19
'''
#Q9
def power(x):
    if n==0:
        return 1
    return x ** power(x,n-1) 
n=int(input())
print(power())

#Q10
def gcd(a,b):
    if n==0:
        return 
    return a//2==0 and b//2==0
gcd(24,18)
print(gcd(24,18))







'''
#lambda funtions
#Even or Odd
def evenorodd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
evenorodd(12)
evenorodd(13)
#lambda function for even or odd
evenorodd_lambda= lambda n: "Even" if n%2==0 else "Odd"
print("evenorodd_lambda:",evenorodd_lambda(5))                   #evenorodd_lambda: Odd
print("evenorodd_lambda:",evenorodd_lambda(52))                  #evenorodd_lambda: Even

#Square of a number
def square(n):
    return(n*n)
square(3)
square(5)
#lamdba funtion for square
squares_lambda= lambda n: n*n
print("Squares_lambda:",squares_lambda(5))
print("squares_lambda:",squares_lambda(52))                    #Squares_lambda: 25
                                                               #squares_lambda: 2704


#map in funtions=
def sqa(l):
    for i in  range(len(l)):
        l[i]**=2
sqa([1,2,3,4,5])
sqa([4,5,6,7])

#map funtion
squl_lambda= list(map(lambda i:i**2, [1,2,3,4,5]))
print("squl_lambda",squl_lambda)                              #squl_lambda [1, 4, 9, 16, 25]

v='aeiou'
squl_lambda= list(map(lambda i:'*' if i  in v else i,'python'))              #squl_lambda pyth*n
print("squl_lambda",''.join(squl_lambda))

l = [[1, 3], [2, 1], [4, 5]]
s = sorted(l, key=lambda i: i[1])
print(s)                                                       #[[2, 1], [1, 3], [4, 5]]
s=sorted([1, 3], [2, 1], [4, 5])(s,key=lambda i:i[-1])
print(s)
l=[[23,34,56],[21,56,89,30],[78,90,54,35],[43,67,3,17]]  
s=sorted(l,key=lambda i: i[0])
print(s)

#Q1
from functools import reduce

n=int(input())
square=lambda n : n*n                  #15
print(square(n))                       #225              

#Q2
from functools import reduce

n=int(input())
iseven=lambda n : True if n%2==0 else False
print(iseven(n))                    #38  #True

#Q3
from functools import reduce

a=int(input())
b=int(input())

iseven= lambda a,b : a if a>b else b           #12  #34  #34
print(iseven(a,b))
'''

#Q4
from functools import reduce
l=[(1,3), (2,5), (6,9)]
print(sorted(l, key = lambda i:i[1],reverse=True))           #[(6, 9), (2, 5), (1, 3)]

#Q5
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda i: i%2==0,l)))                #[2, 4, 6, 8, 10]
    
#Q6
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda i: i*i,l)))                    #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Q7
from functools import reduce
l=['sreekar','sai','srenidhi','harsha']
print(list(map(lambda i: i.upper(),l)))            #['SREEKAR', 'SAI', 'SRENIDHI', 'HARSHA']
   
#Example
def is_palindrome(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return is_palindrome(n[1:-1])
print(is_palindrome("madam"))
















#filter funtion=if the condition is true then it will return the value