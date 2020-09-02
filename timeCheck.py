import time
import calendar

ticks = time.time()
print ("Number of ticks since 1/1/1970: ", ticks)

localtime = time.localtime(time.time())
print (localtime)

formattedtime = time.asctime(time.localtime(time.time()))
print (formattedtime)

cal = calendar.month(2020, 8)
print (cal)

