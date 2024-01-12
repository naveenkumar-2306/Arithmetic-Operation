from datetime import datetime
d = int(input("Enter the date"))
m = int(input("enter the month"))
y = int(input("Enter the year"))
date = datetime(y,m,d)
print(date)
week = date.strftime('%A')
print(week)
