#Type Conversion (Type Casting)
#Type conversion in Python refers to converting the value of one data type to another using built-in functions such as int(), float(), str(), bool(), list(), tuple(), set(), and dict().
#1.Coverting from int
a = 10
int_a = 10
print(a)                           #10
print(float(a))                    #10.0
print(complex(a))                  #(10+0j)
print(bool(a))                     #True
print(str(a))                      #10
#print(list(a))                     #print(list(a)) :TypeError: 'int' object is not iterable=(like a string, list, tuple, etc.) as its argument. An integer is not iterable, so attempting to convert it directly to a list raises a TypeError .
#print(tuple(a))                    #print(tuple(a)):TypeError: 'int' object is not iterable=(like a string, list, tuple, etc.) as its argument. An integer is not iterable, so attempting to convert it directly to a list raises a TypeError .
#print(dict(a))                     #print(dict(a)):ypeError: 'int' object is not iterable=(like a string, list, tuple, etc.) as its argument. An integer is not iterable, so attempting to convert it directly to a list raises a TypeError .
#print(set(a))                      #print(set(a)):TypeError: 'int' object is not iterable=ypeError:=(like a string, list, tuple, etc.) as its argument. An integer is not iterable, so attempting to convert it directly to a list raises a TypeError .

#2.Converting from float
b = 33.7
float_b = 33.7
print(int(b))                         #33
print(complex(b))                     #(33.7+0j)
print(str(b))                         #33.7
print(bool(b))                        #True
#print(tuple(b))                        #Error:he tuple() function also expects an iterable. Passing an integer to it results in a TypeError for the same reason as above.
#print(set(b))                          #Similar to list(), the set() function requires an iterable. Since an integer isn't iterable, this operation raises a TypeError.
#print(dict(b))                         #The dict() function expects an iterable of key-value pairs (like a list of tuples). An integer doesn't meet this requirement, leading to a TypeError .
#print(list(b))                         #he list() function expects an iterable (like a string, list, tuple, etc.) as its argument. An integer is not iterable, so attempting to convert it directly to a list raises a TypeError .

#3. Converting from string
s = 'student'
string_d = 'student'
#print(int(s))                          #int not Invalid literal
s1 = '20'
print(int(s1))                          #20
#print(float(s))                        #Invalid literal
print(float(s1))                        #20.0
#print(complex(s))                      #it will not allow the str
print(list(s))                          #['s', 't', 'u', 'd', 'e', 'n', 't']           
print(bool(s))                          #True
print(tuple(s))                         #('s', 't', 'u', 'd', 'e', 'n', 't')
print(set(s))                           #{'d', 'e', 'u', 't', 's', 'n'}
#print(dict(s))                         #Needs key-value pair structure

#4. Converting from list
l = [10, 30, 50, 90]
list_d =  [10, 30, 50, 90]
#print(int(l))                         #Not allowed
#print(float(1))                       #Not allowed
print(str(l))                          #[10, 30, 50, 90]
print(bool(l))                         #True
print(tuple(l))                        #(10, 30, 50, 90)
print(set(l))                          #{10, 50, 90, 30}
#print(dict(l))                        #Needs list of key-value pairs

#5. Converting from tuple
t = (39, 89, 56, 45, 12)
tuple = (39, 89, 56, 45, 12)
#print(int(t))                         #Not allowed
#print(float(t))                       #Not allowed 
print(str(t))                          #(39, 89, 56, 45, 12)
print(bool(t))                         #True
print(list(t))                         #[39, 89, 56, 45, 12]
print(set(t))                          #{39, 12, 45, 56, 89}
#print(dict(t))                        #Must be tuple of key-value pairs

#6. Converting from set

set = {4, 5, 3, 8, 9, 0, 1}
#print(int(set))                         #Not allowed
#print(float(set))                       #Not allowed
print(str(set))                          #{0, 1, 3, 4, 5, 8, 9}
print(bool(set))                         #True
print(tuple(set))                        #(0, 1, 3, 4, 5, 8, 9)
set1 = {1, 2, 3, 4, 5}                    
print(tuple(set1))                        #(1, 2, 3, 4, 5)
print(list(set))                          #[0, 1, 3, 4, 5, 8, 9]
#print(dict(set))                         #Must be iterable of key-value pairs


#7. Converting from dict
dict = {1:7, 2:8, 3:7}
#print(int(dict))                         #Type error
#print(float(dict))                       #Type error
print(str(dict))                          #{1: 7, 2: 8, 3: 7}
print(bool(dict))                         #True
print(tuple(dict))                        #(1, 2, 3)
print(set(dict))                          #{1, 2, 3}
print(list(dict))                         #[1, 2, 3]	



#8. Converting from bool

b1 = False

print(int(b1))                              #0
print(float(b1))                            #0.0
print(str(b1))                              #'False'
#print(list(b1))                            #TypeError: 'list' object is not iterable
#print(tuple(b1))                           #TypeError: 'tuple' object is not iterable
#print(set(b1))                             #TypeError: 'set' object is not iterable
#print(dict(b1))                            #TypeError: 'bool' object is not iterable
  
b2 = True

print(int(b2))                               #1
print(float(b2))                             #1.0
print(str(b2))                               #True
#print(list(b2))                             #TypeError: 'list' object is not iterable
#print(tuple(b2))                            #TypeError: 'tuple' object is not iterable
#print(set(b2))                              #TypeError: 'set' object is not iterable
#print(dict(b2))                             #TypeError: 'bool' object is not iterable


#9. Dictionary Conversion

d = [('name', 'ram'), ('batch', '21'), ('cource', 'Datascience')]
#print(int(d))                               #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#print(float(d))                             #TypeError: float() argument must be a string or a real number, not 'list'
print(str(d))                                #[('name', 'ram'), ('batch', '21'), ('cource', 'Datascience')]
print(bool(d))                               #True
print(tuple(d))                              #(('name', 'ram'), ('batch', '21'), ('cource', 'Datascience'))
print(set(d))                                #{('name', 'ram'), ('cource', 'Datascience'), ('batch', '21')}
print(list(d))                               #[('name', 'ram'), ('batch', '21'), ('cource', 'Datascience')]
