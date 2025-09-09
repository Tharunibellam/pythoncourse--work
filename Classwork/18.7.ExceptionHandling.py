#Except=keyword()direction the of the code to move where to go
#Exception=find the what is the error (if u don't know the what type of error go write Exception)
#Method1
try:
    a=10
    a=a+19
    l=[1,3,4]
    k=[2]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number: "))
    print(b)
    c=1+"1"
except NameError:
    print("a is not defined")
except IndexError:
    print("You have entered the out of range value")
except KeyError:
    print("Key is not define")    
except ValueError:
    print("Enter the proper data type")
except TypeError:
    print("you can't add 2 diff types")

'''4
Enter a number: 34
34
you can't add 2 diff types
'''
#Method2
#how can we catch the multiple error at a time
try:
    a=10
    a=a+19
    l=[1,3,4]
    k=[2]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number: "))
    print(b)
    c=1+12
except (NameError,IndexError,KeyError,ValueError,TypeError) as e:
    print(f"Error occured: {e}")
'''Enter a number: dbjhd
Error occured: invalid literal for int() with base 10: 'dbjhd'
output2
4
Enter a number: 67
67
Error occured: list index out of range'''
#Method3 
#best method to go
try:
    l=[1,3,4]
    k=l[8]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number: "))
    print(b)
    c=1+12
except Exception as e:
    print(f"Error occured: {e}")
'''4
Enter a number: jhegd
Error occured: invalid literal for int() with base 10: 'jhegd
output 2
output2
4
Enter a number: 67
67
No Errors
13'''
#Method4
#when ur not having any error in try black then else will be print
try:
    l=[1,3,4]
    k=[8]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number: "))
    print(b)
    c=1+12
except Exception as e:
    print(f"Error occured: {e}")

else:
    print("No Errors")
    print(c)
'''4
Enter a number: gdjgf
Error occured: invalid literal for int() with base 10: 'gdjgf
output2
4
Enter a number: 67
67
Error occured: list index out of range'''

#Method5
#if have error and no error this black will excuted succesfully
try:
    l=[1,3,4]
    k=[8]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number: "))
    print(b)
    c=1+12
except Exception as e:
    print(f"Error occured: {e}")

else:
    print("No Errors")
    print(c)

finally:
   print("----------code executed------------------")   
'''4
Enter a number: 43
43
No Errors
13
----------code executed------------------'''
#
try:
    amount=int(input("Enter the amount: "))
    if amount<0:
        raise ValueError("Enter the positive value")
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("No errors")
    print("you can withdraw")
finally:
    print("--------Remove your card---------------")
'''Enter the amount: 56
No errors
you can withdraw
--------Remove your card---------------'''


