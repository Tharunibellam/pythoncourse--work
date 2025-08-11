










































import platform
print(platform.system())               #Windows
print(platform.release())              #11
print(platform.processor())            #Intel64 Family 6 Model 154 Stepping 4, GenuineIntel



import math

print(math.sqrt(25))                  #5.0
print(math.pow(3,4))                  #81
print(round(45.8))                    #46

print(math.fabs(-40))                 #40.0
print(abs(-23))                       #23
print(math.factorial(6))              #720
print(math.gcd(8,24))                 #8
print(math.log(5))                    #1.6094379124341003
print(math.sin(1))                    #0.8414709848078965
print(math.degrees(36))               #2062.648062470964
print(math.tan(45))
print(math.radians(30))

import random

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))
names=['sreenidhi','kavya','Rupasree','sumathi']
print(random.choice(names))
print(random.choices(names,k=3))      #Rupasree
random.shuffle(names)                 #['Rupasree', 'sreenidhi', 'Rupasree']
print(names)                          #['sreenidhi', 'sumathi', 'Rupasree', 'kavya']

import collections
W='python program java program html file css file'
d=collections.Counter(W)  
print(d)                                        #Counter({' ': 7, 'r': 4, 'a': 4, 'p': 3, 'o': 3, 'm': 3, 'l': 3, 't': 2, 'h': 2, 'g': 2, 'f': 2, 'i': 2, 'e': 2, 's': 2, 'y': 1, 'n': 1, 'j': 1, 'v': 1, 'c': 1})

import collections
w='Hello world program python program java program'.split() 
d=collections.Counter(w)
print(d)                          #Counter({'program': 3, 'Hello': 1, 'world': 1, 'python': 1, 'java': 1})

import collections
w=(1,3,4,5,6,7,9,2)
d=collections.Counter(w)
print(d)                         #Counter({1: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1, 2: 1})


import collections
s='abcdef'
d=collections.defaultdict(int)
for i in s:
    d[i]+=1
print(d)                           #defaultdict(<class 'int'>, {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})

import collections
s='abcdef'
d=collections.defaultdict(float)
for i in s:
    d[i]+=1
print(d)                           #defaultdict(<class 'float'>, {'a': 1.0, 'b': 1.0, 'c': 1.0, 'd': 1.0, 'e': 1.0, 'f': 1.0})

import collections
w='Hello world program python program java program'.split() 
d=collections.defaultdict(int)
for i in w:
    d[i]+=1
print(d)                          #defaultdict(<class 'int'>, {'Hello': 1, 'world': 1, 'program': 3, 'python': 1, 'java': 1})

import collections
s='abcdef'
d=collections.defaultdict(str)
for i in range(1,7):
    d[i]+s[i-1]
print(d)                       #defaultdict(<class 'str'>, {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''})

import collections
d=collections.defaultdict(int)
l=[1,2,3,4,5,6,7,8,1,2,3,3,5,1,7,9]
for i in l:
    d[i]+=1
print(d)                  #defaultdict(<class 'int'>, {1: 3, 2: 2, 3: 3, 4: 1, 5: 2, 6: 1, 7: 2, 8: 1, 9: 1})

import collections
d=collections.defaultdict(str)
l=[1,2,3,4,5,6,7,8,1,2,3,3,5,1,7,9]
for i in l:
    d[i]+="string"
print(d)                      #defaultdict(<class 'str'>, {1: 'stringstringstring', 2: 'stringstring', 3: 'stringstringstring', 4: 'string', 5: 'stringstring', 6: 'string', 7: 'stringstring', 8: 'string', 9: 'string'})

from collections import deque
l=deque()
l.appendleft(78)
l.appendleft(23)
l.pop()
l.append(45)
l.append(12)
l.popleft()
l.pop()
print(l)                        #deque([45])

from itertools import combinations,permutations
print(list(combinations('ABCD',3)))           #[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
print(list(combinations('12345',4)))           #[('1', '2', '3', '4'), ('1', '2', '3', '5'), ('1', '2', '4', '5'), ('1', '3', '4', '5'), ('2', '3', '4', '5')] 

