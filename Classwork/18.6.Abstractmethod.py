#“You don’t need to know how it works, just how to use it.”
#AbstractMethod
from abc import ABC, abstractmethod
class Bankaccount(ABC):
    def deposit(self):
        print("You can deposit amount")
    def Checkbalance(self):
        print("You can check your balance")
    @abstractmethod
    def withdraw(self):
        pass
    def viewhistory(self):
        print("You can check the history")
class CurrentAccount(Bankaccount):
    def withdraw(self):
        print("You can withdraw Extra amount also")
class SavingAccount(Bankaccount):
    def withdraw(self):
        print("You can withdraw amount")

mani=CurrentAccount()
shanmukh=SavingAccount()
mani.Checkbalance()
mani.deposit()
mani.viewhistory()
mani.withdraw()
shanmukh.Checkbalance()
shanmukh.deposit()
shanmukh.viewhistory()
shanmukh.withdraw()

'''You can check your balance
You can deposit amount
You can check the history
You can withdraw Extra amount also
Ypu can check your balance
You can deposit amount
You can check the history
You can withdraw amount'''




#Example2
from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass
    
class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order: Check chef availability, estimate time, assign delivery.")

class GroceryOrder(Order):
    def process_order(self):
        print("Processing Grocery Order: Check inventory per item, bag & dispatch.")

class MedicineOrder(Order):
    def process_order(self):
        print("Processing Medicine Order: Validate prescription, assign secure courier.")

class CloudKitchenOrder(Order):
    def process_order(self):
        print("Processing Cloud Kitchen Order: Prepare dynamically, generate OTP.")

class TiffinOrder(Order):
    def process_order(self):
        print("Processing Tiffin Subscription: Schedule weekly deliveries, manage preferences.")

class PetSuppliesOrder(Order):
    def process_order(self):
        print("Processing Pet Supplies Order: Check pet product categories and ship.")

class MeatOrder(Order):
    def process_order(self):
        print("Processing Meat/Seafood Order: Confirm freshness, assign chilled delivery.")

class CakeOrder(Order):
    def process_order(self):
        print("Processing Cake Order: Custom baking, time-sensitive packaging.")

class PartyOrder(Order):
    def process_order(self):
        print("Processing Party Order: Bulk cooking, team coordination, special packaging.")

class JuiceOrder(Order):
    def process_order(self):
        print("Processing Fresh Juice Order: Immediate prep, cold packaging.")


def handle_order(order: Order):
    order.process_order()

orders = [
    FoodOrder(),
    GroceryOrder(),
    MedicineOrder(),
    CloudKitchenOrder(),
    TiffinOrder(),
    PetSuppliesOrder(),
    MeatOrder(),
    CakeOrder(),
    PartyOrder(),
    JuiceOrder()
]

for order in orders:
    handle_order(order)

#Output:
'''Processing Food Order: Check chef availability, estimate time, assign delivery.
Processing Grocery Order: Check inventory per item, bag & dispatch.
Processing Medicine Order: Validate prescription, assign secure courier.
Processing Cloud Kitchen Order: Prepare dynamically, generate OTP.
Processing Tiffin Subscription: Schedule weekly deliveries, manage preferences.
Processing Pet Supplies Order: Check pet product categories and ship.
Processing Meat/Seafood Order: Confirm freshness, assign chilled delivery.
Processing Cake Order: Custom baking, time-sensitive packaging.
Processing Party Order: Bulk cooking, team coordination, special packaging.
Processing Fresh Juice Order: Immediate prep, cold packaging.'''

