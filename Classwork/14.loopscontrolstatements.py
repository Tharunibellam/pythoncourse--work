#Control Statements
#Loops help automate repetitive tasks
#FOR LOOP=A for loop is used to iterate over items like lists, strings, or ranges.
'''for i in range(5):  # i takes values from 0 to 4
    print(i)       # prints numbers 0 through 4

# Example2: Using a for loop to iterate over a list and print each item squared

numbers = [1, 2, 3, 4, 5]  # List of numbers

for num in numbers:
    squared = num ** 2
    print(f"The square of {num} is {squared}")                  #The square of 1 is 1
                                                                #The square of 2 is 4
                                                                #The square of 3 is 9
                                                                #The square of 4 is 16
                                                                #The square of 5 is 25

#Example:3 
# User's workout record over a week
workout_log = [1, 1, 1, 0, 1, 1, 0]
current_streak = 0
longest_streak = 0
for day in workout_log:
   if day == 1:
    current_streak += 1
    if current_streak > longest_streak:
       longest_streak = current_streak

else:
    current_streak = 0 # Streak breaks
print("Longest workout streak:", longest_streak)          #Longest workout streak: 5                                                        



#WHILE LOOP=A while loop repeats a block of code as long as a condition is True.
# Initialize the condition variable
count = 0  

# Continue to loop while count is less than 5
while count < 5:
    print(f"Iteration {count + 1}")
    
    # Update condition variable to eventually break the loop
    count += 1

print("Loop has ended.")                           #Iteration 1                           #Iteration 1
                                                   #Iteration 2
                                                   #Iteration 3
                                                   #Iteration 4
                                                   #Iteration 5
                                                   #Loop has ended.

#Example
# Simulating incorrect login attempts
correct_pin = "1234"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
   entered_pin = input("Enter your PIN: ")
   if entered_pin == correct_pin:
     print("Login successful!")
     break
   else:
     print("Incorrect PIN. Try again.")
     attempts += 1

else:
  print("Account locked due to too many failed attempts.")     '''         #Enter your PIN: 546
                                                                        #Incorrect PIN. Try again.
                                                                        #Enter your PIN: 707
#Example
count = 1  # Initialize counter

while count <= 5: 
    print(f"Count is: {count}")
    count += 1  # Increment the counter to avoid infinite loop1234
                                                                        #Count is: 1
                                                                        #Count is: 2
                                                                        #Count is: 3
                                                                        #Count is: 4
                                                                        #Count is: 5

#FOR LOOP WITH ELSE=The else block runs only if the loop completes without encountering a break.
# 1 = Unread, 0 = Read
notifications = [0, 0, 0, 1]
for notification in notifications:
 if notification == 1:
  print("You have unread notifications!")
  break

else:
 print("All caught up!")                  #You have unread notifications!
#Example                                                       
numbers = [1, 5, 43, 2, 7, 9, 19, 10]
target = 100

for num in numbers:
    if num == target:
        print("Target found, exiting loop.")
        break
else:
    print("Target not found. Loop completed all items.")            #Target not found. Loop completed all items.

#WHILE LOOP WITH ELSE=Just like with for, the else runs only if the while loop completes without a break.
i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("Liftoff!")          #Liftoff!

#Example
nums = [2, 4, 6, 8, 10]
target = 7
i = 0

while i < len(nums):
    if nums[i] == target:
        print("Found target:", target)
        break
    i += 1
else:
    print("Target not found.")            #Target not found.
#Example
while i < len(nums):
    n = nums[i]
    if n > 1:
        d = 2
        while d < n:
            if n % d == 0:
                print("Composite found:", n)
                break
            d += 1
        else:
            i += 1
            continue
        break
else:
    print("No composite numbers.")                   #No composite numbers.
#break
#Example – for loop:
for i in range(5):
    if i == 3:
        break  # exit loop early when i == 3
    print(i)                                      # Output: 0,1,2
#Example – while loop:
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1                                      # Output: 0,1,2

#break Statement in Python
for i in range(5):
    if i == 3:
        continue  # skip printing 3
    print(i)                                  # Output: 0,1,2,4

#Example – while loop:
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)                                      #Output: 1,3,5

#assert
x = 10
assert x > 0, "x must be positive"
x = 5
assert x > 0, "x must be positive"

#Example – in a function for sanity checks:

x = "hello"
assert x == "hello"
# nothing happens because condition is True

assert x == "goodbye", "x must be 'goodbye'"
                                                    # raises: AssertionError: x must be 'goodbye'

