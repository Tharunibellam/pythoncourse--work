#tables program
'''num=int(input("Enter the table num: "))
for i in range(1,21):
    print(f'{num} * {i} = {num*i}')                       #Enter the table num: 18
#18 * 1 = 18                                            
18 * 2 = 36
18 * 3 = 54
18 * 4 = 72
18 * 5 = 90
18 * 6 = 108
18 * 7 = 126
18 * 8 = 144
18 * 9 = 162
18 * 10 = 180
18 * 11 = 198
18 * 12 = 216
18 * 13 = 234
18 * 14 = 252
18 * 15 = 270
18 * 16 = 288
18 * 17 = 306
18 * 18 = 324
18 * 19 = 342
18 * 20 = 360   

#range
s='vidhya vilok sreenivasulu samatha sreevachala'.lower()
n=len(s)
ch=input("Enter the char: ")

for i in range(n):
    if s[i]==ch:
     print(ch,i)             #Enter the char: e
                                    #e 15
                                    #e 16
                                    #e 36
                                    #e 37   

#index
products=['cycle','watch','moblie','laptop','mouse']
items=input("Enter the items: ").split()

for i in items:
    if i in products:
       print(products.index(i),i)
    else:
        print(F"{i} is not available")                            #Enter the items: cycle moblie laptop mouse watch tv 
                                                                  #0 cycle
                                                                  #2 moblie
                                                                  #3 laptop
                                                                  #4 mouse
                                                                  #1 watch
                                                                  #tv is not available '''

#login email
'''
email,pwd='abc@gmail.com','xyz@789'
max_attempts=5
while max_attempts>0:
    useremail=input("Enter the email: ")
    password=input("Enter the password: ")
    if useremail==email and pwd==password:
        print("Login successful")
        break
    else:
        print("Invalid Login")
    max_attempts-=1
else:
    print("Try after some time")
'''
#output:Enter the email: hhfyd
'''Enter the password: jfuf
Invalid Login
Enter the email: dfjhh
Enter the password: jfhj
Invalid Login
Enter the email: jdfjj
Enter the password: nfdjje
Invalid Login
Enter the email: jfje
Enter the password: jfjj
Invalid Login
Enter the email: ehu
Enter the password: jje
Invalid Login
Try after some time'''
#output:
'''Enter the email: kjgu
Enter the password: hugy
Invalid Login
Enter the email: gyug
Enter the password: iuh
Invalid Login
Enter the email: abc@gmail.com
Enter the password: xyz@789
Login successful 
'''



