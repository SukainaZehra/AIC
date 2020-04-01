#calculate number of days between two dates
import datetime
from datetime import date
"""def differ_days(date1, date2):

    a = date1
    b = date2
    return (a-b).days
print()
print(differ_days((date(2016,10,12)), date(2015,12,10)))
print(differ_days((date(2016,3,23)), date(2017,12,10)))
print()"""
d1 = date(2016,12,12)
d2 = date(2015,12,12)
print((d1-d2).days)