#1.Numeric type
#a.int-integer

a =10      #like count,order,numbers
print(type(a))  #<class 'int'>

#b.float-Floating-point

a=674.9     #price,discount,ratings
print(type(a))   #<class 'float'>

#c.complex-complex Numbers

z =5+2j     #e-commerce used in specialized analytics or image processing
print(type(z))   #<class 'complex'>

#2.Sequence Types

#a.str_string
a="Rohit sharma"
print(type(a))   #<class 'str'>

#List-List

l=["Mobiles","Home","Headphones"]
print(type(l))     #<class 'list'>

#tuple-Tuple

t=(12.97,77.832,2.2)
print(type(t))    #<class 'tuple'>

#3.Set Type

#a.set-set

s={"tharuni","sreenivasulu","samatha","sreevachala"}
print(type(s))    #<class 'set'>

#b.frozenset-Immutable set

frozen_tags=frozenset(["sale","limited edition","trending"])
print(type(frozen_tags))     #<class 'frozenset'>

#MappingType

#a.dict-Dictionary

s={"name":"tharuni","cource":"DS","batch":14}

print(type(s))   #<class 'dict'>

#5.Bool-Boolean
a = True
b = False
 
 #using Boolean in a condition

print(type(a))   #<class 'bool'>
print(type(b))   #<class 'bool'>



#5.None type


print(type(None))  #<class 'NoneType'>




