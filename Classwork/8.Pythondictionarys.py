#Dictionary
#A dictionary in Python is an ordered, mutable collection that stores key-value pairs.Unlike lists or tuples, which are iexed by position, dictionaries are indexed by unique keys.
#1. Introduction to Dictionary
#A dictionary is defined using curly braces {}, where each key is followed by a colon :, and the key-value pairs are separated by commas.

#Syntax of a Dictionary:
#dictionary_name = {key1: value1, key2: value2, key3: value3}

student = {"name": "Ram",
           "cource": "DS",
           "batch" : "15"
           }
print(student)                                  #{'name': 'Ram', 'cource': 'DS', 'batch': '15'}

#Key Features of Dictionaries:Keys must be unique,Keys must be immutable,Values can be of any data type,Dictionaries are mutable.

#2. Dictionary Operations
#2.1 Accessing Values
print(student["name"])                              #Ram
print(student.get("age"))                           #None

#Difference Between dict[key] and dict.get(key)
print(student.get("city","Not Available"))          #Not Available

#2.2 adding and updating items

student["age"] = 23
student["city"] = "New york"
print(student)                                     #{'name': 'Ram', 'cource': 'DS', 'batch': '15', 'age': 23, 'city': 'New york'}

#2.3 Removing Items from a Dictionary
#Using pop()
age = student.pop("age")
print(age)                                          #23
print(student)                                      #{'name': 'Ram', 'cource': 'DS', 'batch': '15', 'city': 'New york'}

#Using del
#del student["course"]
#print(student)

#using popitem()
student.popitem()                         
print(student)                                     #{'name': 'Ram', 'cource': 'DS', 'batch': '15'}

#using clear()
student.clear()
print(student)                                     #{}

#3. Dictionary Built-in Methods
#3.1 Dictionary Methods for Accessing Data

person = {'full name':'google','id':'212t1','course':'Ds','batch':'15','brach':'ECE'}
#dict.get(key,default)=Returns the value for the given key; returns default if key is not found
print(person.get("full name"))                       #google
print(person.get("brach"))                           #ECE
print(person.get("age"))                             #None

#dict.keys()=Returns a view object containing all keys

print(person.keys())                               #dict_keys(['full name', 'id', 'course', 'batch', 'brach']) 
print(list(person.keys()))
#dict.values()=Returns a view object containing all values

print(person.values())
print(list(person.values()))                       #dict_values(['google', '212t1', 'Ds', '15', 'ECE'])        


#dict.items()= Returns a view object containing all key-value pairs as tuples

print(person.items())                             #dict_items([('full name', 'google'), ('id', '212t1'), ('course', 'Ds'), ('batch', '15'), ('brach', 'ECE')])

#3.2 Dictionary Methods for Adding and Updating Data
#dict.update(new_dict)=Merges another dictionary into the current dictionary
person = {'full name':'google','id':'212t1','course':'Ds','batch':'15','brach':'ECE'}

print("before:",person)                             #before: {'full name': 'google', 'id': '212t1', 'course': 'Ds', 'batch': '15', 'brach': 'ECE'}
person.update({"state":"andhra pradesh"})
print("After:",person)                              #After: {'full name': 'google', 'id': '212t1', 'course': 'Ds', 'batch': '15', 'brach': 'ECE', 'state': 'andhra pradesh'}

#dict.setdefault(ke y, default)=Returns value of key; if key does not exist, inserts it with de ault value
print(person.setdefault("name","prathana"))
print(person)                                     #prathana{'full name': 'google', 'id': '212t1', 'course': 'Ds', 'batch': '15', 'brach': 'ECE', 'state': 'andhra pradesh', 'name': 'prathana'}

print(person.setdefault("city", "unknow"))
print(person)                                      #unknow{'full name': 'google', 'id': '212t1', 'course': 'Ds', 'batch': '15', 'brach': 'ECE', 'state': 'andhra pradesh', 'name': 'prathana', 'city': 'unknow'}

#3.3 Dictionary Methods for Removing Data
#dict.pop(key,default)=Removes and returns value of the specified key
person = {'full name':'google','id':'212t1','course':'Ds','batch':'15','brach':'ECE'}

val = person.pop('course')
print(val)                   #batch': '15', 'brach': 'ECE', 'state': 'andhra pradesh', 'name': 'prathana', 'city': 'unknow'}
print(person)                #Ds{'full name': 'google', 'id': '212t1', 'batch': '15', 'brach': 'ECE'}

val = person.pop('id')
print(val)
print(person)                  #212t1{'full name': 'google', 'batch': '15', 'brach': 'ECE'} 

#dict.popitem()=Removes and returns the last inserted key-value pair
person = {'full name':'google','id':'212t1','course':'Ds','batch':'15','brach':'ECE'}
person.popitem()
print(person)                      #{'full name': 'google', 'id': '212t1', 'course': 'Ds', 'batch': '15'}

#dict.clear() Removes all key-value pairs, making the dictionary empty

person = {'full name':'google','id':'212t1','course':'Ds','batch':'15','brach':'ECE'}
person.clear()
print(person)                           #{}

#del dict[key]= Deletes a specific key from the dictionary
data = {'a':10, 'b':20, 'c':30}
del data['b']
print(data)                               #{'a': 10, 'c': 30}

#4. Built-in Functions for Dictionaries=Python provides several built-in functions that can be used with dictionaries.
#len(dict)=Returns the number of items in the dictionary

person = {'full name':'google','id':'212t1','course':'Ds','batch':'15','brach':'ECE'}
print(len(person))                     #5

#Max
print(max(person))                     #v

#Min
print(min(person))                     #batch

#Sorted()
print(sorted(person))                  #['batch', 'brach', 'course', 'full name', 'id']

#5. Nested Dictionaries=A dictionary can contain another dictionary as its value.
child1 = {"name": "jerry", "year": 2004}
child2 = {"name": "Tom", "year": 2007}
myfamily = {"child1": child1, "child2": child2}
print(myfamily["child2"]["name"])                           #Tom
print(myfamily["child1"]["year"])                           #2004

#6. Dictionary Comprehension=You can create dictionaries dynamically using dictionary comprehension.
squares = {n: n*n for n in range(1, 8)}
print(squares)                                     #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

#7. Real-Time Problems Using Dictionaries =Problem 1: Find the Student with the Highest Marks
students = {
"venky": 39,
"sai": 82,
"sree": 78
}
top_student = max(students, key=students.get)
print(top_student)                                   #sai

#Count the Frequency of Words in a Sentence
def word_count(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
text = 'the quick brown fox jumps over the lazy dog the fox was quick'
print(word_count(text))                                    #{'the': 3, 'quick': 2, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'was': 1}



