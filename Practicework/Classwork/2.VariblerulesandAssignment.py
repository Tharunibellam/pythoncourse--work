myvar=10   #valid var
myVar=10   #valid var
myVar=10   #valid var
Myvar=10    #valid var
Myvar=10    #valid var
my_var=10   #valid var
#my@var=10   #syntaxError:Cannot assign to expression here.Maybe you meant '==' instead of '='?
#1myvar=10   #syntaxError:invalid decimal literal
_myvar=10    #valid var
#@myvar=10   #syntaxError:invalid syntax.Matbe you meant '==' or ':='?

#my var=10   #syntaxError:invalid syntax
myvar1=10   #case-sensitive
myvar2=20   #case-sensitive
print(myvar1,myvar2)  #10 20

a=10  #Assignment
a,b,c=10,20,30   #Multiple Assignment
print(a,b,c)     #10 20 30

a=b=c=10   #same value Assignment
print(a,b,c)    #10 10 10

a=10
b=20
print("Before swapping(a,b):",a,b)  #Before swapping(a,b): 10 20
a,b=b,a
print("After swapping(a,b):",a,b)   #After swapping(a,b): 20 10
a,b=10,20
del (a,b)
