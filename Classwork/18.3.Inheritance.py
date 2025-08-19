#Single Inheritance
class A:
    def display_a(self):
        print("Parents class A")   #single child
class B:
    def display_b(self):
        print("Child class B<-A") #Parents
a=A()
a.display_a()                #Parents class A
b=B()
b.display_b()                #Child class B<-A
a.display_a()                #Parents class A

#2. Inheritance=multiple parents and only one child
class A:
    def display_a(self):
        print("Parent class A")   
class B:
    def display_b(self):
        print("parent class B") 
class C:
    def display_c(self):
        print("Parent class C")  
class D(A,B,C):
    def display_d(self):
        print("Child class A,B,C->D")
d=D()
d.display_a()                     #Parent class A
d.display_b()                     #parent class B
d.display_c()                     #Parent class C
d.display_d()                     #Child class A,B,C->D

#Multilevel Inheritance=
class A:
    def display_a(self):
        print("Parent class A")   
class B(A):
    def display_b(self):
        print("parent class B") 
class C(B):
    def display_c(self):
        print("Parent class C")  
class D(C):
    def display_d(self):
        print("Child class A,B,C->D")
d=D()
d.display_a()                     #Parent class A
d.display_b()                     #parent class B
d.display_c()                     #Parent class C
d.display_d()                     #Child class A,B,C->D

#Hierarchical Inheritance=Multiple subclasses inherit from a single superclass.
class A:
    def display_a(self):
        print("Parent class A")   
class B(A):
    def display_b(self):
        print("parent class B") 
class C(A):
    def display_c(self):
        print("Parent class C")  
class D(A):
    def display_d(self):
        print("Child class A,B,C->D")
b=B()
b.display_a()   
b.display_b()

c=C()
c.display_a() 
c.display_c() 

d=D()
d.display_a()
d.display_d()

#1.Single Inheritance=One child class inherits from one parent class.

class Parent:
    def show(self):
        print("I am Parent class")

class Child(Parent):   # Inheriting Parent
    def display(self):
        print("I am Child class")

obj = Child()
obj.show()     # From Parent
obj.display()  # From Child

#2. Multiple Inheritance
class Father:
    def skill(self):
        print("Father: I can drive")

class Mother:
    def talent(self):
        print("Mother: I can cook")

class Child(Father, Mother):   # Inheriting both
    def hobby(self):
        print("Child: I love painting")

obj = Child()
obj.skill()   # Father: I can drive
obj.talent()  # Mother: I can cook
obj.hobby()   # Child: I love painting

#3. Multilevel Inheritance=A class inherits from another child class → forms a chain.
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def show(self):
        print("Hello from Parent")

class Child(Parent):
    def display(self):
        print("Hello from Child")

obj = Child()
obj.greet()   # From Grandparent
obj.show()    # From Parent
obj.display() # From Child
'''Hello from Grandparent
Hello from Parent
Hello from Child'''
#4.Hierarchical Inheritance=Multiple child classes inherit from the same parent.
class Parent:
    def show(self):
        print("I am Parent class")

class Child1(Parent):
    def child1_fun(self):
        print("I am Child1")

class Child2(Parent):
    def child2_fun(self):
        print("I am Child2")

obj1 = Child1()
obj1.show()
obj1.child1_fun()

obj2 = Child2()
obj2.show()
obj2.child2_fun()
'''I am Parent class
I am Child1
I am Parent class
I am Child2'''
#5. Hybrid Inheritance=Combination of more than one type of inheritance (like Multiple + Hierarchical).
class A:
    def methodA(self):
        print("Class A method")

class B(A):
    def methodB(self):
        print("Class B method")

class C(A):
    def methodC(self):
        print("Class C method")

class D(B, C):   # Hybrid (Multiple + Hierarchical)
    def methodD(self):
        print("Class D method")

obj = D()
obj.methodA()  # From A method
obj.methodB()  # From B method
obj.methodC()  # From C method
obj.methodD()  # From D method
'''
Single → One parent → One child

Multiple → Multiple parents → One child

Multilevel → Chain of inheritance

Hierarchical → One parent → Multiple children

Hybrid → Mix of above
'''

class Status2015:
    def view(self):
        print("You can view status")
    def reply(self):
        print("You can reply")
    def caption(self):
        print("You can add caption")

class Status2020(Status2015):
    def uploadImg(self):
        print("You can upload Image")
    def uploadVid(self):
        print("You can upload video -30 sec")
    def privacy(self):
        print("You can select who can see your status")

class Status2023(Status2020):
    def ProfilePrivacy(self):
        print("You can update the profile privacy")
    def reaction(self):
        print("You can send reactions")           
    def like(self):
        print("You can like the status")


class Status2024(Status2020):
    def statusrings(self):
        print("Color is added to the status display")
    def mute(self):
        print("You can mute the other's status")
    def filters(self):
        print("You can filters")

    
class Status2025(Status2023,Status2024):
    def music(self):
        print("You can add music")
    def mention(self):
        print("You can mention them")
    def collab(self):
        print("You can share your status from insta or fb")
    def voicenote(self):
        print("You can voice note")


print("\nNandhu")       
Nandhu= Status2015()
Nandhu.view()
Nandhu.reply()
Nandhu.caption()

print("\nMounika")
Mounika=Status2020()
Mounika.uploadImg()
Mounika.uploadVid()
Mounika.privacy()
Mounika.view()
Mounika.caption()

print("\nVandhana")
Vandhana=Status2023()
Vandhana.uploadImg()
Vandhana.uploadVid()
Vandhana.privacy()
Vandhana.view()
Vandhana.reply()
Vandhana.caption()
Vandhana.ProfilePrivacy()
Vandhana.reaction()
Vandhana.like()

print("\nPavani")
Pavani=Status2024()
Pavani.uploadImg()
Pavani.uploadVid()
Pavani.privacy()
Pavani.view()
Pavani.reply()
Pavani.caption()
Pavani.statusrings()
Pavani.mute()
Pavani.filters()


print('\nSwetha')
Swetha=Status2025()
Swetha.uploadImg()
Swetha.uploadVid()
Swetha.privacy()
Swetha.view()
Swetha.reply()
Swetha.caption()
Swetha.statusrings()
Swetha.mute()
Swetha.filters()
Swetha.ProfilePrivacy()
Swetha.reaction()
Swetha.like()

'''Nandhu
You can view status
You can reply
You can add caption

Mounika
You can upload Image
You can upload video -30 sec
You can select who can see your status
You can view status
You can add caption

Vandhana
You can upload Image
You can upload video -30 sec
You can select who can see your status
You can view status
You can reply
You can add caption
You can update the profile privacy
You can send reactions
You can like the status

Pavani
You can upload Image
You can upload video -30 sec
You can select who can see your status
You can view status
You can reply
You can add caption
Color is added to the status display
You can mute the other's status
You can filters

Swetha
You can upload Image
You can upload video -30 sec
You can select who can see your status
You can view status
You can reply
You can add caption
Color is added to the status display
You can mute the other's status
You can filters
You can update the profile privacy
You can send reactions
You can like the status'''