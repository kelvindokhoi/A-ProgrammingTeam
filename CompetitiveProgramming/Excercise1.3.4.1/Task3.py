#print out the day of the week and how many day has elapsed since that day

from datetime import *

weekdays = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}

day, month, year = map(int, input().split())
input_date = date(day,month,year)

print(weekdays[input_date.weekday()])

today = date.today()
print(f"{(today-input_date).days} days passed")