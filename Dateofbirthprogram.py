# date-of-birth-program
import calendar
from datetime import datetime
now=datetime.now()
the=now.date()
that=list(str(the))
these=int(that[0]+that[1]+that[2]+that[3])
yourage=input('what is your age as of today: ')
the=int(these)-int(yourage)
month=input('what month were you born: ')
date=input('what is the date of your birth: ')
cal=calendar.weekday(int(the),int(month),int(date))
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months=['January','February','March','April','May','June','July','August','September','October','November','December']
print('You where born on ',days[cal],date, months[int(month)-1], the)

#HAKIZA WALTER
