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

from datetime import date,time, datetime,timedelta
today= date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())
d = date(2025,12,31)
dt = time(23,59,12)
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

print(now.strftime('%d/%m/%y'))
print(now.strftime('%d %b, %y'))
print(now.strftime('%d %B, %Y'))
print(now.strftime('%d %B, %H:%M:%S'))
print(now.strftime('%a %d %B, %y %H:%M:%S %P'))
print(now.strftime('%A, %d %B, %Y %H:%M:%S %P'))
fdate=today - timedelta(day=7)
fmins=now + timedelta(minute=30)
print(fdate,fmins)

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











