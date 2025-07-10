#Tuples
#A tuple is an immutable,ordered collection of elements.
#faster than lists because they are immutable,can store any of data(int,float,list etc)

#type creation syntax:
#Emty tuple
empty_tuple = ()
print(empty_tuple)                             #()

#single-elements tuple(note the trailing comma)
single_tuple = (17,)
print(single_tuple)                            #(17,)

#Multi-element tuple
my_tuple = (10, "python", 2.6, 3+8j)
print(my_tuple)                                 #(10, 'python', 2.6, (3+8j))

#without parentheses (implicit tuple creation)
implicit_tuple = 1, 2, 3
print(implicit_tuple)                          #(1, 2, 3)

#2.Accessing tuple elements
# Access elements using zero-based indexing

#a.Indexing
t = (30, 49,32.0,57)
print(t[0])                                 #30
print(t[2])                                 #32.0
print(t[1])                                 #49

#b.Negative indexing
t = (9.0, "name", 3+6j, -89)
print(t[-1])                                 #-89
print(t[-2])                                 #(3+6j)
print(t[-3])                                 #name
print(t[-4])                                 #9.0

#Slicing=Extract a portion of the tuple using slicing ([start:end:step]).

tuple = (9.0, "name", 3+6j, -89)
print(tuple[1:])                       #('name', (3+6j), -89)
print(tuple[:2])                       #(9.0, 'name')
print(tuple[0:4])                      #(9.0, 'name', (3+6j), -89)
print(tuple[::3])                      #(9.0, -89)
print(tuple[1::])                      #((3+6j), -89)

#3.Operation on tuples
#a. Concatenation
tuple1 = (30, 49,32.0,57)
tuple2= (9.0, "name", 3+6j, -89) 
tuple = tuple1 + tuple2
print(tuple)                            #(30, 49, 32.0, 57, 9.0, 'name', (3+6j), -89)


#b.Repetition=Repeat the elements of a tuple using the * operator.

tuple = (200, "student", 4+7j, 90.7)
print(tuple*6)                           #(200, 'student', (4+7j), 90.7, 200, 'student', (4+7j), 90.7, 200, 'student', (4+7j), 90.7, 200, 'student', (4+7j), 90.7, 200, 'student', (4+7j), 90.7, 200, 'student', (4+7j), 90.7)

#c. Membership Testing=Check if an element is present in the tuple using the in or not in keywords.
tuple = (200, "student", 4+7j, 90.7, False, {1, 2, 3, 4})
print("student" in tuple)               #True
print({1, 2, 3, 4} in tuple)            #True
print(False not in tuple)               #False
print(True not in tuple)                #True
print([1, 30, 46] not in tuple)         #True
print(300+5j in tuple)                  #False

#d. Tuple Unpacking=Assign tuple elements to multiple variables.
tuple = (200, 55, 67, 98, 100)
a, b, c, d, e = tuple
print(a)                                   #200
print(b)                                   #55
print(c)                                   #67
print(d)                                   #98
print(e)                                   #100

#4. Tuple Methods
#count(x) Counts the number of occurrences of the tuple
tuple = ( 200, "student", 1, 2, 3, 4)
print(tuple.count("student"))                                 #1                                                               #7
print(tuple.count(60))                                        #0

#Built-in function for tuples
#min()
tuple = (200, 150, 55, 67, 88, 200, 88, 55, 150, 77)
print(min(tuple))                                             #55                            

#len

tuple = (200, 150, 55, 67, 88, 200, 88, 55, 150, 77)
print(len(tuple))                                              #10

#Max()
tuple = (200, 150, 55, 67, 88, 200, 88, 55, 150, 77)
print(max(tuple))                                                #200

#sum()
tuple = (200, 150, 55, 67, 88, 200, 88, 55, 150, 77)

print(sum(tuple))                                                 #1130

#tuple(iterable)
tuple = (1, 30, 49, 76, [2, 4, 8, 5])
tuple[4].append(1)
print(tuple)


#6.immutability and Tuple Behaviour
nested_tuple = (1,[2,3])
nested_tuple[1][1] = 200                                    #(1,[2,200])
print(nested_tuple)