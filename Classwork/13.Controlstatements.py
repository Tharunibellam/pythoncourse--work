#Control Statements
#Loops help automate repetitive tasks
#FOR LOOP=A for loop is used to iterate over items like lists, strings, or ranges.
for i in range(5):  # i takes values from 0 to 4
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
  print("Account locked due to too many failed attempts.")              #Enter your PIN: 546
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
