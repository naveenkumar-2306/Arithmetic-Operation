import datetime
from datetime import timedelta


print("\nQuestion 1 \n")

date_store = datetime.datetime.now()

print("Current date and time :: ",date_store)

##Creating a date and time object

x = datetime.datetime(2024,1,9,15,22,3)

print("Day of x :: ",x.strftime("%c"))

print("\n Question 2 \n")

## Subtract a week
date_reduce = 7

print("The date stored before the day is ::",x.day)

print("Day of x :: ",x.strftime("%A"))

new_date = x.day - 7

y = datetime.datetime(2024,1,new_date,20,30,3)

print("The date stored after the day is ::",y.day)

print("Day of y :: ",y.strftime("%A"))

print("\n Question 3 \n")

## Find the day of week of a given date


str_year,str_month,str_date= input("Enter the year,month,date to find the day : ").split()

year = int(str_year)
month = int(str_month)
date = int(str_date)
z = datetime.datetime(year,month,date)
print("Day of z :: ",z.strftime("%A"))

print("\n Question 4 \n")
## Add a week and 12 hours to given date

y = datetime.datetime(2024,1,9,20,30,3)

week = 7

hours = 12

new_date = y + timedelta(weeks=7,hours=12)


print("Date-time after weeks and hours added :: ",new_date)


print("\n Question 5 \n")

## Calculate number of days between two given dates


from datetime import datetime

# Input your two dates in the format 'YYYY-MM-DD'
date1_str = '2022-01-01'
date2_str = '2024-01-09'

# Convert the date strings to datetime objects
date1 = datetime.strptime(date1_str, '%Y-%m-%d')
date2 = datetime.strptime(date2_str, '%Y-%m-%d')

# Calculate the difference between the two dates
days_difference = (date2 - date1).days

print(f'Number of days between {date1_str} and {date2_str}: {days_difference} days')









