# print number of days between two date
from datetime import datetime ,timedelta

date1 = input("Input date1 in dd-mm-yyyy")
date2 = input("Input date2 in dd-mm-yyyy")
d1 = datetime.strptime(date1, '%d-%m-%Y').date()
d2 = datetime.strptime(date2, '%d-%m-%Y').date()
num = d1-d2
print(num)
