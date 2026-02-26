import datetime as s
from datetime import timedelta
b = s.datetime(2026,12,12,23,59,59)
print(b)
b = b + timedelta(days=20) # timedelta it's just a period of time , in this example i add 20 days to date b
print(b)
x =s.datetime.now()
print(type(x))
print(x) # it'll output the current date and time
print(x.strftime("%A")) #it'll do the weekday
print(x.strftime("%a")) #it'll do the weekday but it's concised version Wednesday -> Wed
y = x.year
print(y)# this is the current year
print(x.strftime("%y")) # this is the first two digits of the year now is 2026 it will output 26
print(x.strftime("%B")) # it will output the current name of the month 
print(x.strftime("%m")) # it will output the current number of the month 
print(x.strftime("%d")) # it will output the current day of the month 
time = s.time(12,59,59)
print(time)
dt1 = timedelta(hours=1,minutes=40,seconds=10)
dt2 = timedelta(hours=10,minutes=50,seconds=50)
time1 = dt1.total_seconds()
time2 = dt2.total_seconds()
print(time1)
print(time2)
print(time2-time1)
print(x.strftime("%H:%M:%S %B")) # we also can combine them so now it shows up the time and the month's name
if b > x:
    print("We're in the future")
else:
    print("we are not in the future")