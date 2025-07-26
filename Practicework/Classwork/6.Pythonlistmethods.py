#Lists
#1. Basic features o f lists = ordered,Mutable,Indexed,Allow Duplicates,Heterogeneous,Dynamic.
#2.Creating Lists=lists can be created using square brackets [] or the list() constructor
#2.1 Empty List

my_list = []      #Empty list: []
my_list2 = list() #Using list() constructor
print("Empty list:", my_list2)

#2.2 Lists with Elements

numbers = [5,1,8,10,15]      
course = ["datascience,dataanalytics,python full stack"]   
mixed = [15, "datascience", 15.9, False]    
print("Numbers:", numbers)        # Numbers: [5, 1, 8, 10, 15]
print("course:", course)          #course: ['datascience,dataanalytics,python full stack'] 
print("Mixed types:", mixed)      #Mixed types: [15, 'datascience', 15.9, False]

#2.3 Nested Lists
nested_list = [[1, 2, 3], ["a", "b", "c"], [True,False]]
print("Nested list:", nested_list)    #Nested list: [[1, 2, 3], ['a', 'b', 'c'], [True, False]] 

#2.4Listing list() constructor

list_from_tuple = list((1, 2, 3))   # Converting tuple to list
string_to_list = list("Python")
print("from tuple:", list_from_tuple)     #from tuple: [1, 2, 3]
print("from string:", string_to_list)     #from string: ['P', 'y', 't', 'h', 'o', 'n']

               
#3.Accessing Elements in a list
#3.1 using indexing (positive & Negative)

list = ["banana", "mango", "apple", "grapes"]

print(list[0])    #banana
print(list[1])    #mango
print(list[-2])   #apple
print(list[-1])   #grape

#3.2 using slicing
list = ["banana", 20, "mango", 10,"apple", 33, "grapes"]

print(list[2::])     #['mango', 10, 'apple', 33, 'grapes']
print(list[:3])      #['banana', 20, 'mango']
print(list[4:])      #['apple', 33, 'grapes']
print(list[::4])     #['banana', 'apple']
print(list[-6:-1])   #[20, 'mango', 10, 'apple', 33]
print(list[1:5])     #[20, 'mango', 10, 'apple']

#4.Modifying Lists
#4.1 Changing Elements

numbers = [20, 35, 45]
numbers[2] = 10
print(numbers)         #[20, 35, 10]


#4.2 Adding Elements

# Starting list

list = [10, 20, 30, False, 50.6, "string", [5, 1, 2], (2+3j), {"name": "Append"}, {8, 3, 6,9} ]
#Append(l):adds l to end
list.append(70)
print("append:", list)      #Append:[10, 20, 30, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, 70]

list.append(6+1j)
print("append:", list)      #Append:[10, 20, 30, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, 70, (6+1j)]

list.append("Python")
print("append:", list)      #Append:[10, 20, 30, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, 70, (6+1j), 'Python']

#Extend(iterable): adds all elements from another iterable

list.extend([60, 80])
print("exetend:", list)        #exetend: [10, 20, 30, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, 70, (6+1j), 'Python', 60, 80]    

list.extend(["DS", "DA"])
print("extend:", list)         #extend: [10, 20, 30, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, 70, (6+1j), 'Python', 60, 80, 'DS', 'DA']


#insert(index, list): inserts x at given index

list.insert(0, 1)
list.insert(4, True)
list.insert(-6, "insert")
print("insert:", list)          #insert: [1, 10, 20, 30, True, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, 70, 'insert', (6+1j), 'Python', 60, 80, 'DS', 'DA']


#Remove(l)): removes first occurenece of list

list.remove(True)
list.remove(20)
print("remove:", list)          # remove: [10, 30, True, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, 70, 'insert', (6+1j), 'Python', 60, 80, 'DS', 'DA']

#pop([index]): removes and return element at index (default last)

list.pop()
list.pop(-5)
print("pop:", list)               #pop: [10, 30, True, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, 70, 'insert', 'Python', 60, 80, 'DS']

# clear(): removes all elements

list1 = [10, 20, 30, "claer", "remove"]
list1.clear()
print("clear:", list1)                 #clear: []

#index(list): return index of first list
print("index of 30:", list.index(30))        #index of 30: 1
print("index of 80:", list.index(80))        #index of 80: 14
print("index of 2+3j:", list.index(2+3j))    #index of 2+3j: 7


#count(): number of times list apperas

print("count of 50.6",list.index(50.6))       #count of 50.6 4
print("count of 80", list.index(80))          #count of 80 14
print("count of 2+3j:", list.index(2+3j))     #count of 2+3j: 7

# sort(): sorts ascending; reverse=True for descending

list = [10, 20, 30, False, 50.6]
list.sort(reverse=True)
print("sort:", list)             #sort: [50.6, 30, 20, 10, False]
list = [1,2,3,3,11,5,0,2,True,4,7,8,4,False,5,6,10]
list.sort(reverse=True)
print("sort asc:",list)           #sort asc: [11, 10, 8, 7, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, True, 0, False] 

list.sort(reverse=False)
print("sort desc:", list)        #sort desc: [0, False, 1, True, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 10, 11]

#reverse():reverses list in-place
list1 = [1,2,3,3,11,5,0,2,True,4,7,8,4,False,5,6,10]
list2 = [10, 20, 30, False, 50.6, "string", [5, 1, 2], (2+3j), {"name": "Append"}, {8, 3, 6,9} ]
print("reverse:", list1)       #reverse: [1, 2, 3, 3, 11, 5, 0, 2, True, 4, 7, 8, 4, False, 5, 6, 10]
print("reverse:", list2)       #reverse: [10, 20, 30, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}]      #

# copy(): shallow copylist2 = [10, 20, 30, False, 50.6, "string", [5, 1, 2], (2+3j), {"name": "Append"}, {8, 3, 6,9} ]

list1 = [1,2,3,3,11,5,0,2,True,4,7,8,4,False,5,6,10]
k = list1.append(15)
copy_list1 = list1.copy()
list2 = [10, 20, 30, False, 50.6, "string", [5, 1, 2], (2+3j), {"name": "Append"}, {8, 3, 6,9} ]
m = list2.append(-7)
copy_list2 = list2.copy()
print("copy:", copy_list1)         # copy: [1, 2, 3, 3, 11, 5, 0, 2, True, 4, 7, 8, 4, False, 5, 6, 10, 15]               
print("copy:", copy_list2)         # copy: [10, 20, 30, False, 50.6, 'string', [5, 1, 2], (2+3j), {'name': 'Append'}, {8, 9, 3, 6}, -7]    

#sorted(iterable, Key=none,reverse=false)

nums = [2,1,4,5,8]
print(sorted(nums))                  #[1, 2, 4, 5, 8]
print(sorted(nums, reverse=True))    #[8, 5, 4, 2, 1]

#Max(iterable, Key=none) and Min(iterable)
list1 = [1,2,3,3,11,-5,0,2,True,4,7,8,-4,False,5,6,10]
print(max(list1))                     #23
print(min(list1))                     #-5

# withmstrings
list = ["hello world"]
print(max("hello world"))             #w
print(min("helloworld"))              #d

#Using key
str_nums = ["10", "3", "20", "45"]
print(max(str_nums, key=int))         #45
print(min(str_nums, key=int))         #3

#+sum(iterable, strat=0)
nums = [3,7,0,8]
print(sum(nums))                      #18              
print(sum(nums, 100))                 #118

#\len(iterable)
items = [5,8,9,12]
print(len(items))                      #4
print(len("python"))                   #6

#any(iterable) and all(iterable)

flags = [False, True, False]
print(any(flags))            #True(at least one True)
print(all(flags))            #False(not all are True)

print(any([]))                #False(empty iterable)
print(all([]))                #True(vacuous truth)


