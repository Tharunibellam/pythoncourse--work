#.....................Sets..........................
#A set is an unordered, mutable collection of unique elements.

#Creating a set with unique elements
set = {10, 20, 30,}
print(set)                              #{10, 20, 30}

#Creating an empty set (use set() function, not {})
empty_set = ()

#Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {20, 40, 50, 30, 20, 30}
print(set_with_duplicates)

#set properties
#Unordered,unique elements,Mutable,Immutable elements only.
# This will raise a TypeError
#invalid_set = {[1, 2], 3}                    # Lists are mutable and cannot be
#added to a set

#3.Operation o