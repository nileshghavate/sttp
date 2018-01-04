
import time  # This is required to include time module.


ticks = time.time()
print ("Number of seconds since 12:00am, January 1, 1970:", ticks)
print (time.localtime());

print (time.localtime())
localtime = time.asctime( time.localtime())
print ("Local current time :", localtime)


import calendar
cal = calendar.month(2018, 1)
print (cal)

print (calendar.leapdays(2010,2030))
print (calendar.weekday(2018,1,4))
