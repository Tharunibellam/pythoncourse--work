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














