import datetime
from datetime import timedelta

year = int(raw_input("Year: "))
month = int(raw_input("Month: "))
day = int(raw_input("Day: "))
hour = int(raw_input("Hour: "))
minute = int(raw_input("Minute: "))
second = int(raw_input("Second: "))

t1 = datetime.datetime(year=year, month=month, day=day, hour=hour,\
        minute=minute)
t2 = datetime.datetime.now()

print t1
print t2

tdelta = t1 - t2

print "There are " + str(tdelta.total_seconds()/60/60/24) + " days,"
print str(tdelta.total_seconds()/60/60) + " hours"
print str(tdelta.total_seconds()/60) + " minutes"
print str(tdelta.total_seconds()) + " seconds"
