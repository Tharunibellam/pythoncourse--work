#Read mode
#if have no file it show an error

try:
    file=open('PracticeWork .txt','r')
except FileNotFoundError:
    print("File is not present")
    

'''
try:
    file=open('PracticeWork.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    read=file.read()
    file.seek(0)
    readlines=file.readlines()
    file.seek(0)
    readline=file.readline()
    print(f"\nFile content using read():\n{read}")
    print(f"\nFile content using readlines():\n{readlines}")
    print(f"\nFile content using readline():\n{readline}")
    file.close(0)
finally:
    print("Rest of the code")

#Write mode
#if we have no file then i tcreat a new file
try:
    file=open('dsda.txt','w')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam')
    file.close()
finally:
    print("Rest of the code")

#append mode 
try:
    file=open('dsda.txt','a')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam\n')
    file.close()
finally:
    print("Rest of the code")

#append + read
try:
    file=open('dsda.txt','a+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code")
#monday we have exammonday we have exam
monday we have exam

Rest of the code#
#read+=write + read
try:
    file=open('dsda.txt','r+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code")
#monday we have exam
nday we have exam
monday we have exam

Rest of the code#
#write+=read + write
try:
    file=open('dsda.txt','w+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code")
#monday we have exam

Rest of the code#
#with open as how to it automatically close it
with open('dsda.txt','r+') as file:
    file.write('\nFile operations')
    file.seek(0)
    print(file.read())

import os
print(os.getcwd())
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')

#
#rmdir=remove
import os
if os.path.exists('DSDA'):
    os.rmdir('DSDA')

#
import os
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
    os.makedirs('DSDA')

import os
import shutil
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
    os.makedirs('DSDA/1415')
#os.rmdir('DSDA')
shutil.rmtree('DSDA')

'''

