#subtract a week from given date
from datetime import datetime, timedelta
d = int(input("Enter the date"))
m = int(input("enter the month"))
y = int(input("Enter the year"))
date = datetime(y,m,d)
print(date)
num = int(input("Enter number of days"))
date1 = date - timedelta(days=num)
print(date1)
