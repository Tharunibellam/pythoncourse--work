#OOP (Object-Oriented Programming) is a way of writing code by grouping data and functions together into classes and objects.
#Class = Blueprint (like a design of a car 🚗)
#Object = Real thing made from blueprint (like your car)
'''Class → Blueprint of an object.

Object → Instance of a class.

Attributes → Variables inside a class.

Methods → Functions inside a class.

Inheritance → A class can use features of another class.

Encapsulation → Hiding details, exposing only what is needed.

Polymorphism → Same function name, different behaviors.'''

#OOPS Example in python
# Class (Blueprint)
class BankAccount:
    # Constructor (runs when object is created)
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance = {self.balance}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance = {self.balance}")
        else:
            print("Insufficient balance!")

    # Method to show account info
    def show_info(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


# ------------------------------
# Creating Objects (Real Accounts)
acc1 = BankAccount("Tharuni", 5000)
acc2 = BankAccount("Rahul", 1000)

# Using Methods
acc1.show_info()
acc1.deposit(2000)
acc1.withdraw(3000)

acc2.show_info()
acc2.withdraw(1500)  # Will show insufficient balance
'''Owner: Tharuni, Balance: 5000
Deposited 2000. New Balance = 7000
Withdrew 3000. New Balance = 4000
Owner: Rahul, Balance: 1000
Insufficient balance!'''