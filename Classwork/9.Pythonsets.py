#.....................Sets..........................
#A set is an unordered, mutable collection of unique elements.

#Creating a set with unique elements
set = {10, 20, 30,}
print(set)                              #{10, 20, 30}

#Creating an empty set (use set() function, not {})
empty_set = ()

#Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {20, 40, 50, 30, 20, 30}
print(set_with_duplicates)              #{40, 50, 20, 30}

#set properties
#Unordered,unique elements,Mutable,Immutable elements only.
# This will raise a TypeError
#invalid_set = {[1, 2], 3}                    # Lists are mutable and cannot be
#added to a set

#3.Operation of sets =Python provides several set operations that mimic mathematical set theory.
#a. Membership Testing
set = {20, 33, 42, 78}
print(20 in set)                             #True
print(48 in set)                             #False
print(70 not in set)                         #True
print(33 not in set)                         #False

#b. Union (| or union() method)=Combines elements from two sets (removes duplicates).Syntax: set1 | set2 or set1.union(set2)
set1 = {20, 34, 76}
set2 = {89, 34, 10, 73}
result = set1 | set2
print(result)                                  #{73, 34, 20, 89, 10, 76}

#c. Intersection (& or intersection() method)=Returns common elements between two sets.Syntax: set1 & set2 or set1.intersection(set2)
result = set1 & set2
print(result)                                  #{34}

#d. Difference (- or difference() method)Returns elements in the first set but not in the second set.Syntax: set1 - set2 or set1.difference(set2)
set1 = {34, 367, 89, 11}
set2 = {54, 67, 49, 200}                
result = set1 - set2
print(result)                                  #{89, 34, 11, 367}

#e.Symmetric Difference (^ or symmetric_difference() method)=Returns elements in either set1 or set2 but not both.
#Syntax: set1 ^ set2 or set1.symmetric_difference(set2)
set1 = {34, 367, 89, 11}
set2 = {54, 67, 89, 200}
result = set1 ^ set2
print(result)                                   #{34, 67, 200, 11, 367, 54}

#f.Subset (<= or issubset() method)=Checks if all elements of one set are present in another. Syntax: set1 <= set2 or set1.issubset(set2)

set1 = {29, 48, 20.5, 45, 56}
set1 = {12, 45, 32, 67}
result1 = set1 <= set2
print(result1)                                  #False

set1 = {20, 34}
set2 = {20, 34, 89, 47, 200}
result = set1 <= set2
print(result)                                  #True

#g. Superset (>= or issuperset() method)=Checks if one set contains all elements of another.Syntax: set1 >= set2 or set1.issuperset(set2)
set1 = {29, 48, 20.5, 45, 56}
set2 = {12, 45, 32, 67}
result1 = set1 >= set2
print(result1)                                  #False

set1 = {20, 34, 300}
set2 = {20, 34}
result = set1 >= set2
print(result)                                   #True

#h. Disjoint Sets (isdisjoint() method)=Returns True if two sets have no common elements.
set1 = {29, 48, 20.5, 45, 56}
set1 = {12, 45, 32, 67}
print(set1.isdisjoint(set2))                    #False

#4. Built-in Methods for Sets
#add(element)=Adds an element to the set
my_set = {1, 2, 3, (2+6j), "python", (1, 20, 34)}
my_set.add(8)
print("after add(8):", my_set)                                 #after add(8): {1, 2, 3, (2+6j), 8, (1, 20, 34), 'python'} 
my_set.add(False) 
print("after add(False)):", my_set)                            #after add(False)): {False, 1, 2, 3, (2+6j), 'python', 8, (1, 20, 34)}

#remove(element)=Removes an element; raises an error if the element doesn’t exist
my_set.remove("python")
print("After remove(python):", my_set)                          #After remove(2): {False, 1, 2, 3, (2+6j), 8, (1, 20, 34)}  
#except keyError:
#my_set.remove(3.8)
#print("element (3.8):", my_set)

#discard(element) Removes an element; does not raise an error if the element doesn’t exist
my_set.discard(2)
print("After discard(2):", my_set)                               #After discard(2): {False, 1, 3, (2+6j), 8, (1, 20, 34)}    
my_set.discard(3.9)
print("After discard(3.9):", my_set)                             #After discard(3.9): {False, 1, 3, (2+6j), 8, (1, 20, 34)} 

#pop()=Removes and returns an arbitrary element
my_set.pop()
print("After pop():", my_set)                                    #After pop(): {1, 3, (2+6j), 8, (1, 20, 34)}

#clear():Removes all elements from the set
my_set.clear()
print("After clear():", my_set)                                  #After clear(): set()

#union(other_set)=Returns the union of two sets
set1 = {1, 20, "class", "books", "pen", 30.8}
set2 = {59, "id", "name", "group", 20, 60}
set = set1 | set2
print(set)                                                        #{1, 'class', 'group', 'name', 'books', 'id', 20, 'pen', 59, 60, 30.8}

set1 = {1, 2, 3, 6}
set2 = {2, 4, 7, 9}
set = set1.union(set2)
print(set)                                                         #{1, 2, 3, 4, 6, 7, 9}
#intersection(other_set)=Returns the intersection of two sets
set1 = {1, 20, "class", "books", "pen", 30.8}
set2 = {59, "id", "name", "group", 20, 60}
set = set1 & set2
print(set)                                                          #{20}

set1 = {1, 2, 3, 6}
set2 = {2, 4, 7, 9}
print(" using intersection():", set1.intersection(set2))            #using intersection(): {2}
print(set)
#Symmetric Difference: in either set but not both
set1 = {1, 20, "class", "books", "pen", 30.8}
set2 = {59, "id", "name", "group", 20, 60}
set = set1 ^ set2
print(set)                                                          #using  symmetric_difference(): {'pen', 1, 'books', 'class', 30.8, 'name', 'group', 'id', 59, 60}                                                        #

set4 = {1, 2, 3, 6}
set5 = {2, 4, 7, 9}
print(" using symmetric_difference():", set4.symmetric_difference(set5))
print(set)                                                             # using symmetric_difference(): {1, 3, 4, 6, 7, 9}
# Difference: in set1 but not in set2
set1 = {1, 20, "class", "books", "pen", 30.8}
set2 = {59, "id", "name", "group", 20, 60}
set = set1 - set2
print(set)                                                             #{'pen', 1, 'class', 'books', 30.8}

set1 = {1, 2, 3, 6}
set2 = {2, 4, 7, 9}
print(" using difference():", set1.difference(set2))                   #using difference(): {1, 3, 6}
print(set)   

#update(other_set): Adds elements from another set to the current set
set1 = {1, 2, 3, 6}
set2 = {2, 4, 7, 9}
set1.update(set2)                         
print("updated set1:", set1)                                           #updated set1: {1, 2, 3, 4, 6, 7, 9}
set2.update(set1)                                                      
print("updated set2:", set2)                                           #updated set2: {1, 2, 3, 4, 6, 7, 9}

#intersection_update(other_set): Updates the set with the intersection of itself and another set
set1 = {1, 2, 3, 70,  6}
set2 = {2, 4, 7, 70,  9}
set1.intersection_update(set2)                         
print(" intersection_updated set1:", set1)                              #intersection_updated set1: {2, 70}                                      #updated set1: {1, 2, 3, 4, 6, 7, 9}
set2.intersection_update(set1)                                                      
print("intersection_updated set2:", set2)                               #intersection_updated set2: {2, 70}

#difference_update(other_set):Updates the set by removing elements found in another set
set1 = {1, 2, 3, 70,  6}
set2 = {2, 4, 7, 70,  9}
set1.difference_update(set2)                         
print(" difference_updated set1:", set1)                                #difference_updated set1: {1, 3, 6}
set2.difference_update(set1)                                                      
print("difference_updated set2:", set2)                                 #difference_updated set2: {2, 4, 70, 7, 9}

#symmetric_difference_update(other_set):Updates the set with the symmetric difference
set1 = {1, 2, 3, 70,  6}
set2 = {2, 4, 7, 70,  9}
set1.symmetric_difference_update(set2)                         
print("After symmetric_ difference_updated:", set1)                      #After symmetric_ difference_updated: {1, 3, 4, 7, 6, 9} 

#copy(): Returns a shallow copy of the set
set1 = {1, 2, 3, 70,  6}
print("copied:",set1)                                                    #copied: {1, 2, 3, 70, 6}
set2 = {2, 4, 7, 70,  9}
print("copied set:",set2)                                                #copied set: {2, 4, 70, 7, 9}

#isdisjoint(other_set):Returns True if two sets have no elements in common
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 6, 9}

print("set1 and set2 are disjoint:", set1.isdisjoint(set2))             #set1 and set2 are disjoint: True
print("set1 and set3 are disjoint:", set1.isdisjoint(set3))             #set1 and set3 are disjoint: False

#issubset(other_set):Returns True if the set is a subset of another set
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {2, 6}
print("set_a is subset of set_b:", set_a.issubset(set_b))              #set_a is subset of set_b: True
print("set_c is subset of set_b:", set_c.issubset(set_b))              #set_c is subset of set_b: False

#issuperset(other_set):Returns True if the set is a superset of another set
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3}
set_c = {6, 7}
print("set_a is superset of set_b:", set_a.issuperset(set_b))           #set_a is superset of set_b: True
print("set_a is superset of set_c:", set_a.issuperset(set_c))           #set_a is superset of set_c: False

#5. Built-in Functions for Sets
#len(set):Returns the number of elements in the set
set1 = {1, 20, "class", "books", "pen", 30.8, 59, "id", "name", "group", 20, 60}
print(len(set1))                                                        #11

#max(set):Returns the maximum element in the set
set1 = {1, 20, 16,300, 30.8, 59, 48.0, 20, 60}
print(max(set1))                                                        #300

#min(set):Returns the minimum element in the set
set1 = {1, 20, 16,300, 30.8, 59, 48.0, 20, 60}
print(min(set1))                                                        #1

#sum(set):Returns the sum of all elements in the
set1 = {1, 20, 16,300, 30.8, 59, 48.0, 20, 60}
print(sum(set1))                                                        #534.8

#sorted(set): Returns a sorted list of the set elements
set1 = {1, 20, 16,300, 30.8, 59, 48.0, 20, 60}
print(sorted(set1))                                                     #[1, 16, 20, 30.8, 48.0, 59, 60, 300]



#set(iterable):Converts an iterable (e.g., list, string) to a set
#l = [1,2,3,4,5]
#print(set(l))                             #{1, 2, 3, 4, 5}
#set1 = {1, 2, 3, 4, 5}                    
#print(tuple(set1))                        #(1, 2, 3, 4, 5)

#Immutability and Frozensets
#Frozensets are immutable versions of sets.
# Once a frozenset is created, its elements cannot be changed.
# Useful for creating hashable, immutable collections.

#Frozenset()
fs1 = ([1, 2, 3, 4, 2])
fs2 = (('a', 'b', 'c', 'd', 'b'))
fs3 = ("name", "cource")                                           #{1, 2, 3, 4, 5}

print(frozenset(fs1))                                              #frozenset({1, 2, 3, 4})
print(frozenset(fs2))                                              #frozenset({'a', 'b', 'd', 'c'})
print(frozenset(fs3))                                              #frozenset({'name', 'cource'})