import datetime
mytime = datetime.time(12, 25)
print(mytime)

today = datetime.date.today()
print(today)
print(today.ctime())

# DATE
from datetime import date

date1 = date(2023, 12, 30)
date2 = date(2022, 11, 14)
result = date1 - date2
print(result)
print(type(result))
print(result.days)

from datetime import datetime
datetime1 = datetime(2021, 8, 12, 22, 0)
datetime2 = datetime(2021, 8, 12, 12, 0)
mydiffer = datetime1 - datetime2
print(mydiffer)
print(mydiffer.seconds)
