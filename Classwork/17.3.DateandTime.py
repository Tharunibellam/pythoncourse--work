'''
from datetime import date,time,datetime,timedelta
today= date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

d=date(2025,12,23)
print(d)                       
#Error:month must be in 1..12
#Error:days must be in 1..30 or 1..31
'''
'''2025-08-10
2025
8
10
6
7
2025-12-31'''
'''
from datetime import date,time,datetime,timedelta
today= date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

d=date(2025,12,31)
t = (24,47,58)
now=datetime

now=datetime.now()
print(now)
'''
#output:
'''2025-08-10
2025
8
10
6
7
2025-08-10 11:39:14.693232'''
'''
from datetime import date,time,datetime,timedelta
today= date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

d=date(2025,12,31)
t = time(14,47,58)
print(d,t)

# hour must be in 0..23
# sec must be in 0..59
# min must be in 0..59
'''
'''2025-08-10
2025
8
10
6
7
2025-12-31 14:47:58'''
'''
from datetime import date,time, datetime,timedelta
today= date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())
d=date(2025,12,31)
dt=time(23,59,12)
dt = datetime(2024,12,7,22,14,56)
print(dt)
now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
'''
'''2025-08-10
2025
8
10
6
7
2024-12-07 22:14:56
2025-08-10 12:28:03.700613
2025
8
10
12
28
3
'''

from datetime import date, time, datetime, timedelta

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

d = date(2025, 12, 31)
dt = time(23, 59, 12)
dt = datetime(2024, 12, 7, 22, 14, 56)
print(dt)

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(now.strftime('%d/%m/%y'))
print(now.strftime('%d %b, %y'))
print(now.strftime('%d %B, %Y'))
print(now.strftime('%d %B, %H:%M:%S'))
print(now.strftime('%a %d %B, %y %H:%M:%S %p'))
print(now.strftime('%A, %d %B, %Y %H:%M:%S %p'))

# Corrected part
fdate = today - timedelta(days=7)
fmins = now + timedelta(minutes=30)
print(fdate, fmins)

'''
2025-08-10
2025
8
10
6
7
2024-12-07 22:14:56
2025-08-10 13:06:03.073558
2025
8
10
13
6
3
10/08/25
10 Aug, 25
10 August, 2025
10 August, 13:06:03
'''
#1. Get Current Date and Time

import datetime

now = datetime.datetime.now()
print("Current Date & Time:", now)
print("Date:", now.date())
print("Time:", now.time())

#2. Format Date & Time using strftime()
#Frequently asked about formatting codes (%Y, %m, %d, %H, %M, %S, %A, %B, %p).
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # 2025-08-16 19:45:12
print(now.strftime("%A, %B %d, %Y"))       # Saturday, August 16, 2025
print(now.strftime("%I:%M %p"))            # 07:45 PM

#3. Difference Between Two Dates
date1 = datetime.date(2025, 8, 16)
date2 = datetime.date(2024, 8, 16)

diff = date1 - date2
print("Difference:", diff.days, "days")

#4. Add or Subtract Days from a Date
from datetime import datetime, timedelta

today = datetime.today()
print("Today:", today)

after_10_days = today + timedelta(days=10)
print("After 10 Days:", after_10_days)

before_30_days = today - timedelta(days=30)
print("Before 30 Days:", before_30_days)

#5. Check Leap Year
import calendar

year = 2024
print(year, "is leap year?", calendar.isleap(year))

#6.Print Calendar of a Month/Year
import calendar

print(calendar.month(2025, 8))   # August 2025
print(calendar.calendar(2025))  # Whole year

#7. Convert String to Date
from datetime import datetime

date_string = "16-08-2025"
date_obj = datetime.strptime(date_string, "%d-%m-%Y")
print("Converted Date:", date_obj)

#8. Get Weekday of a Date
import datetime

date_obj = datetime.date(2025, 8, 16)
print("Weekday (0=Mon):", date_obj.weekday())
print("Full Name:", date_obj.strftime("%A"))

#9. Stop Execution for Few Seconds
import time

print("Start")
time.sleep(3)   # Wait for 3 seconds
print("End")
#10. Timer Program (Start & End Time)
import time

start = time.time()
for i in range(1000000):
    pass
end = time.time()

print("Execution Time:", end - start, "seconds")

import calendar 
print ("The calendar of year 2018 is : ") 
print (calendar.calendar(2018)) 

#How do you find yesterday’s, today’s, and tomorrow’s date
from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday, today, tomorrow)

#How to get the day of the week for a given date?
import calendar
day_index = calendar.weekday(2025, 8, 22)
print(calendar.day_name[day_index])   # Friday

#1. Write code to calculate the number of days between two dates.
from datetime import date
d1 = date(2025, 8, 22)
d2 = date(2026, 1, 1)
print((d2 - d1).days)   # 132


#2. Convert current time to 12-hour format with AM/PM.
from datetime import datetime
now = datetime.now()
print(now.strftime("%I:%M %p"))   # Example: 05:42 PM

#3. Find the last Friday of a given month.
import calendar
from datetime import date

year, month = 2025, 8
last_day = calendar.monthrange(year, month)[1]
d = date(year, month, last_day)

while d.weekday() != 4:   # 4 = Friday
    d = d.replace(day=d.day - 1)

print("Last Friday:", d)

#4. Print all Mondays of a given year.
import calendar

year = 2025
for month in range(1, 13):
    for day in calendar.monthcalendar(year, month):
        if day[0] != 0:   # Monday column is 0
            print(date(year, month, day[0]))
    
#5. Write a program to add 100 days to today’s date.
from datetime import date, timedelta
today = date.today()
future_date = today + timedelta(days=100)
print("100 days later:", future_date)

#6. Find age from date of birth.
from datetime import date
dob = date(2000, 5, 10)
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
print("Age:", age)

#7. Convert timestamp to datetime.
from datetime import datetime
ts = 1692700800   # Example timestamp
print(datetime.fromtimestamp(ts))

#8. Write code to get the week number of a given date.
from datetime import date
d = date(2025, 8, 22)
print(d.isocalendar()[1])   # Week number

#9. Write a program to find leap years between two years.
import calendar
for year in range(2000, 2030):
    if calendar.isleap(year):
        print(year)

#10. Find the difference between two times in hours and minutes.
from datetime import datetime
t1 = datetime.strptime("10:30:00", "%H:%M:%S")
t2 = datetime.strptime("13:45:00", "%H:%M:%S")
diff = t2 - t1
print("Hours:", diff.seconds//3600, "Minutes:", (diff.seconds//60)%60)
