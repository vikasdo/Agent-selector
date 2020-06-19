import time
from operator import gt
from datetime import datetime

a =  datetime.now()
b=datetime.now().hour

print(a,b)
this_morning = datetime(2009, 12, 2, 9, 30)
last_night = datetime(2009, 12, 1, 20, 0)
t=this_morning.time() < last_night.time()
print(t)

datetime1 = datetime.strptime('07/11/2019 02:45PM', '%m/%d/%Y %I:%M%p')
datetime2 = datetime.strptime('08/11/2019 05:45PM', '%m/%d/%Y %I:%M%p')
if datetime1 < datetime2 :
  print("datetime1 is lesser")

timediff = datetime2 - datetime1
print(timediff.seconds)
seconds = timediff.total_seconds()

# Convert seconds to hours (there are 3600 seconds in an hour)
hours = (timediff.seconds) / 3600

# Show the total
print(hours)