import datetime
from datetime import timedelta
import time

'''
year = int(raw_input("Year: "))
month = int(raw_input("Month: "))
day = int(raw_input("Day: "))
hour = int(raw_input("Hour: "))
minute = int(raw_input("Minute: "))
second = int(raw_input("Second: "))
'''

year = 2016
month = 6
day = 3
hour = 1
minute = 1
second = 1

t1 = datetime.datetime(year=year, month=month, day=day, hour=hour,\
        minute=minute)

t2 = datetime.datetime.now()

while(t1>t2):
    t2 = datetime.datetime.now()

    print t1
    print t2

    tdelta = t1 - t2

    days =  int(tdelta.total_seconds()/60/60/24)
    hours = int(tdelta.total_seconds()/60/60 % 24)
    minutes = int(tdelta.total_seconds()/60 % 60)
    seconds = int(tdelta.total_seconds() % 60)

    print days
    print hours
    print minutes
    print seconds
    time.sleep(1)
