#Q1
for row in range(3):
    for col in range(5):
        print(col,end=' ')
    print()

#Q1
for row in range(5):
    for col in range(5):
        print(row,end=' ')
    print()

#Q1
for row in range(8):
    for col in range(5):
        print('*',end=' ')
    print()

#Q1
for row in range(7):
    for col in range(row+1):
        print(row,end=' ')
    print()

for row in range(17):
    for col in range(row+1):
        print('*',end=' ')
    print()


for row in range(7):
    for col in range(col-1):
        print(col,end=' ')
    print()

n=int(input("Enter the  size: "))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()

n=int(input("Enter the  size: "))
for row in range(n):
    for spa in range(n-row-1):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()

    