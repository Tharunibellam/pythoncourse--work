#TRue are False
items = ['shoes','smartwatch','phone',laptop','airpods','toycar']
print('welcome to amazon store'.center(50,'*'))
searchinput=input("Enter the items:").lower()

if searchinput in items:
   print(f"{searchinput} found. Buy now!!!")
else:
   print(f'{searchinput} is out of stock now. we will notify you.')

#Weekend Budget plan
amount=input(input("Enter hte amont you can spend for weekend: "))
if amount>2000:
   print("Trip to goa")
elif amount>15000:
   print("go for shopping")
elif amount>10000:
   print("clublingg")
elif print>5000:
   print("cafe/Dinner")
elif amount>2000:
   print("maintancess")
elif amount>500:
   print("go for movie")
elif amount>100:
   print("enjoy in pg")
else:
   print("sleep and watch movie in phone")

