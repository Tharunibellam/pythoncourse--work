#Regular Expressions (RegEx)
#match = this is a simply check the pattern is starting with the given one
'''
import re
res=re.match(r'hello','hello world')
print(res.group() if res else "No pattern")           #hello

import re
res=re.match(r'[A-Z]','hello world')           # in the code the h is samll letter so No pattern is because of [A-Z] is used
print(res.group() if res else "No pattern")        #No pattern    

import re
res=re.match(r'\d','hello world')               # there is digits so No pattern is printed 
print(res.group() if res else "No pattern")        #No pattern

import re
res=re.match(r'\d{3}','7655645223 world')               
print(res.group() if res else "No pattern")        #765


#search=search is going to search enter pattern and give first accournace in pattern
import re
res=re.search(r'[0-9]','ds-da-14-15')
print(res.group() if res else "No pattern")          #1

import re
res=re.search(r'[0-9]{2}','Tharuni123')
print(res.group() if res else "No pattern")       #12

#findall=dirctly gives  what is asked like if asked for numbers it all the numbers in pattern and if asked for words it gives all the words
import re
res=re.findall(r'[0-9]{2}','PFS-30  & ds-da-14-15')
print(res)                   #['30', '14', '15']


import re
res=re.findall(r'\s','python pythox psthons  pithin')
print(res)             #['python', 'pythox', 'psthons', 'pithin']

import re
res=re.findall(r'\w+','python pythox psthons  pithin')
print(res)

import re
res=re.findall(r'p..h.n','python pythox psthons  pithin')
print(res)
'''
#finditer=the positions  of a pattern and it is lasy loder
#[]=will match if change in pattern  ()=it need to match the pattern length checkiing
import re
res=re.finditer(r'[0-9]{2}','PFS-30  & ds-da-14-15')
for i in res:
    print(i.group(),i.start())

import re
res=re.finditer(r'[0-9]{2,}','PFS-30  & ds-da-14-15')          #[]=will match if change in pattern  ()=it need to match the pattern length checkiing
for i in res:
    print(i.group(),i.start())

#fullmatch=only checks from staring start and check the position
import re
res=re.fullmatch(r'(aeiou)','aeiou')   
print(res.group() if res else "No pattern")                 #aeiou
#+=for repeating the same pattern in the given string at least one the pattern one time
#*=if u have pattern or not it will run
import re
res=re.fullmatch(r'^[6-9]\d{9}','9876543210')
print(res.group() if res else "No pattern")             #9876543210

import re
res=re.fullmatch(r'DA-..','DA-19') #..=it can be any thing followed by the staring
print(res.group() if res else "No pattern")                #DA-19

import re
res=re.fullmatch(r'hi.','hot hit hat hit') #..=it can be any thing followed by the staring
print(res) 
#split()=
import re
res=re.split(r'\s','python pythox pstgoon splleitr')
print(res)

import re
res=re.split(r'[,;"-]','python pythox pstgoon splleitr')
print(res)
#sub=Replaces matches with another string.
import re 
res=re.sub(r'[aeiouAEIOU]','*0*','pyton is a programming Language')
print(res)              #pyt*0*n *0*s *0* pr*0*gr*0*mm*0*ng L*0*ng*0**0*g*0*

