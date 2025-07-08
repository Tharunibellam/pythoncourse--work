#Srrings
#Operations on strings

#1.Concatenation(+)=Joining two or more strings

str1 = "Dad"
str2 = "Mom"
str3 = str1 + " " + str2
print(str3)     #output:Dad Mom

#2.Repetition(*)=Repeating a string multi times

text = "Tharuni"
print("Tharuni " * 5)  #output:Tharuni Tharuni Tharuni Tharuni Tharuni 

#Indexing=Accessing individual characters using indices

s = "Laptap"    #Laptap=012345=-6-5-4-3-2-1
print(s[0])     #output:L
print(s[1])     #output:a 
print(s[3])     #output:t
print(s[-1])    #output:p
print(s[-2])    #output:a

#Slcing=Extracting a part(substring)of the string
s = "Friends"
print(s[0:4]) #output:Frie
print(s[:5])  #output:Frien
print(s[3:])  #output:ends
print(s[2::]) #output:iends
print(s[::3]) #output:Fes
print(s[-1])  #s
print(s[-1:-4:-1])  #sdn(reverse the string)


#5.Membership(in,not in)=Checking if a substring exists within a string
text = "Familymembers"
print("Family" in text)       #output:Ture
print("parents" not in text)  #output:Ture
print("mom" in text)          #output:Flase
print("members" not in text)  #output:Flase


#2.Built-in string function
#1.len()=length of the string

text = "Congratulations"
print(len(text))   #15

#2.max() and min()(based in the ASCII values) (A=65 to Z=90)  (a=97 to z=122)
s = "Life is a long lesson in humility"
print(max("Life is a long lesson in humility"))  #y (y=121)(highest ASCII value)
s = "BestFriends"
print(min("BestFriends"))      #B  (B=66)(lowest ASCII value)

#3.Sorted()
print(sorted("BestFriends"))   #['B', 'F', 'd', 'e', 'e', 'i', 'n', 'r', 's', 's', 't']

#4.Characters(chr)/order(ord) in ASCII values
#ord()
print(ord('F'))  #70(ASCII value)
print(ord('s'))  #115(ASCII value)
print(ord('9'))  #57(ASCII value)

#chr()
print(chr(105))  #i(ASCII value for 105)
print(chr(78))   #N(ASCII value for 78)

#Complete List of python Strings Methods 
#1.Case Conversion method

#Lower()=convert to lowercase
text = "Python is Best"
print(text.lower())    #python is best

#Upper()=convert to uppercase
print(text.upper())     #PYTHON IS BEST

#Capitalize()=First letter uppercase
s = "data science"
print(s.capitalize())    #Data science

#Title()=First letter of each word capitalized

text = "computer"
print(text.title())      #Computer

#Swapcase=Swap lowercase and uppercase

text = "i LiKe BookS"
print(text.swapcase())    #I lIkE bOOKs

#Casefold
text = "KT"
print(text.casefold())   #kt


#2.Alignment & Formatting Method

#Center=Center the (width,fillchar())
s = "Good luck on your exams"
print(s.center(75,'*'))       #**************************Good luck on your exams**************************
print(s.center(55,"."))       #................Good luck on your exams................

#ljust(width,fillcahr)
print(s.ljust(64,"_"))        #Good luck on your exams_________________________________________
print(s.ljust(43,"#"))        #Good luck on your exams####################
#print('s'.ljust(100,' '))+'sree'  

#rjust(width,fillchar)
print(s.rjust(60,"@"))        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Good luck on your exams
print(s.rjust(80,"!"))        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Good luck on your exams
#print('name'.rjust(10,' ')) + 'Sree'

#Zfill(width)

print("70".zfill(10))    #0000000070
print("1596".zfill(0))   #1596
print("0".zfill(5))      #00000

#format


#format_map




#3.Search & Find Methods

#find()=find the value is present in given string or not if not it give -1

text = "Check your internet connection"
print(text.find('u'))       #8
print(text.find('z'))       #-1
print(text.find(text[:10])) #0
print(text.find(text[2:15]))#2
print(text.find('sub'))     #-1(-1 if not found in str)

#rfind()

print(text.rfind('e'))    #24
print(text.rfind('m'))    #-1(-1 if not found in str)
print(text.rfind('y'))    #6

#index()=but rasises an error if not found

print(text.index('C'))    #0
print(text.index('e'))    #2
print(text.index('t'))    #13
#print(text.index('z'))

#rindex()=but rasises an error if not found
print(text.rindex('e'))   #24
print(text.rindex('o'))   #28
print(text.rindex('c'))   #25
#print(text.rindex('z'))

#Count()=how many times sub appears
print(text.count('e'))    #4
print(text.count('c'))    #3
print(text.count(' '))    #3
print(text.count('z'))    #0

#4.String Testing Method(Boolean Result)
#Startswith()=check the strating

text = "Python String methods"
print(text.startswith("Python"))    #True
print(text.startswith("Hello"))     #False
print(text.startswith("P"))         #True

#Endswith()=check the ends


print(text.endswith("methods"))    #True
print(text.endswith("ds"))         #True
print(text.endswith("world"))      #Flase


#3.isalpha()=true when all the characters are alphabetic(no numbers or symbols)

text = "python"
print(text.isalpha())  #True(It not allowing captial)

text1 = "python23"
print(text1.isalpha())  #False(It not numbers)

#4.isalnum()=return true if all characters are alphanumeric(letters or numbers,no symbols)
 
id = "User123"
print(id.isalnum())   #True

id2 = "User@123"
print(id2.isalnum())  #False

#5.islower()=Returns true if all characters are lowercase letters.

text = "python string methods"
print(text.islower())    #True

text = "Python"
print(text.islower())    #False

#6.isupper()=Return True if all the characters are uppercase letters

text1 = "EXPLANATION"
print(text1.isupper())    #True

text2 = "Observation"
print(text2.isupper())    #False

#7.isspace()=Return True if the string only contains whitespace characters(spaces,tabs,)

space = "   "
print(space.isspace())   #True

text = "Space"
print(text.isspace())    #False

#8.istitle()=Return True if the string is in title case()

title = "I am ur bose"
print(title.istitle())    #False

title = "I Am Ur Bass"
print(title.istitle())    #True

#9.isidentifier()Return True if the String is a valid python identifier(used as a variable/function name)

a = "123@abc"
print(a.isidentifier())    #False

b = "abc123"
print(b.isidentifier())     #True

#Strings (isdecimal()isdigit()isnumberic())
#ASCII decimal digits

s = '678'
print(s.isdecimal())         #True
print(s.isdigit())           #True
print(s.isnumeric())         #True

#Arabic-Indic digit

s = '٣' '۲'
print(s.isdecimal())      #True
print(s.isdigit())        #True
print(s.isnumeric())      #True

#Superscript 2

s = '²'
print(s.isdecimal(), s.isdigit(), s.isnumeric())     #False True True

#Fraction one-third
s = '3/6'
print(s.isdecimal(), s.isdigit(), s.isnumeric())     #False False False

#Chinese numeral for five

s = ' wǔ '
print(s.isdecimal(), s.isdigit(), s.isnumeric())     #False False False

#Roman numeral 8

s = 'XIX'
print(s.isdecimal(), s.isdigit(), s.isnumeric())     #False False False


#Alphabetic characters
s = "HelloWorld"
print(s.isalpha())             #  True

s2 = "Hello123"
print(s2.isalpha())            # False

#Contains a dot,not a numeric char
test = "12.3" 
print(test.isdecimal(), test.isdigit(), test.isnumeric())    # False False False 
test =  "19"
print(test.isdecimal(), test.isdigit(), test.isnumeric())    # True True True

#Contains non-numeric character

test =  "20d19"
print(test.isdecimal(), test.isdigit(), test.isnumeric())    # False False False

test =  "hgd"
print(test.isdecimal(), test.isdigit(), test.isnumeric())    # False False False


#5.Replace & Modify Method

#1.Replace(old,new)=Replaces occurrences of old with new.
text = "Python is powerful"
text = "Python is powerful"
print(text.replace(' ',''))           #Pythonispowerful

s = "I like python"
print(s.replace("python","DS"))        #I like DS


#2.translate(table)=Replaces characters using a translation table.

s = "abcde@145"
print(s.translate(str.maketrans("ac@5","xy!*")))          #xbyde!14*


#3.maketrans()=Creates a translation table for translate().(ASCII value)

text = "abcde@145"
print(text.maketrans("ac@5","xy!*"))                      #{97: 120, 99: 121, 64: 33, 53: 42}

#6. Splitting & Joining Methods
#1.split(sep)=split(sep)

#Strip(char)=spliting a string into a list using the specified separator(sep)

text = "apple,banana,cherry,grape"
result1 = text.split(",")  
result2 = text.split('a')   #is not changeing with other key only it is allowing ","
print(result1)               # ['apple', 'banana', 'cherry', 'grape']
print(result2)               #['', 'pple,b', 'n', 'n', ',cherry,gr', 'pe']

#rsplit(sep)=Splits a string into a list from the right the separator

text = "apple,ball,cat,dog,eye,fun"
result1 = text.rsplit(",", 2)   #divide according to the number we have given dived to right
result2 = text.rsplit(",", 3)      
print(result1)                  #['apple,ball,cat,dog', 'eye', 'fun'] 
print(result2)                   #['apple,ball,cat', 'dog', 'eye', 'fun']


#3.splitlines()=split a string at line breaks(\n)and return a list of lines

text = '''apple 
ball 
cat 
dog 
eye 
fun'''
print(text.splitlines(' '))              #['apple \n', 'ball \n', 'cat \n', 'dog \n', 'eye \n', 'fun']

#join(iterable)=Joins elements with a separator.

cars = ('BMW', 'Ferrari', 'Jeep', 'Porsche')
print('@'.join(cars))                 #BMW@Ferrari@Jeep@Porsche
print('_'.join(cars))                 #BMW_Ferrari_Jeep_Porsche
print('1'.join(cars))                 #BMW1Ferrari1Jeep1Porsche
print(', '.join(cars))                #BBMW, Ferrari, Jeep, Porsche

#partition(sep)=Splits into a 3-part tuple at first sep.

x = "Python Strings . Methods"
print(x.partition('.'))               #('Python Strings ', '.', ' Methods')

#rpartition(sep)=Splits into a 3-part tuple at last sep.

x = "5.Python Strings . Methods"
print(x.rpartition('.'))              #('5.Python Strings ', '.', ' Methods')

#7. Whitespace & Trimming Methods
#strip(chars)=Removes leading and trailing characters (default: spaces).

t = "....example..."
print(t.strip('.'))

t = "          python string methods         "
print(t.strip())                                        #python string methods

#lstrip(chars)=Removes leading characters.
t = "          Hello world           "
print(t.lstrip())                                        # #Hello world


#rstrip(chars)=Removes trailing characters.

t = "**pythonprogram***"
print(t.rstrip())                                     
#encode(encoding)=Converts the string to bytes.

text = "Hello 🙂"
print(text.encode())                   #b'Hello \xf0\x9f\x99\x82'     



#decode(encoding)=Converts bytes back to string.
s=text.encode()
print(s.decode())                     #Hello 🙂
