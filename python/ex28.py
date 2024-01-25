# find the day of the week of a given date

import datetime

date = input ("enter '%d/%m/%y': ")
given_date = datetime.datetime.strptime(date, '%d/%m/%y')

day_of_week = given_date.weekday()
days = [ 'mon' , 'tue' , 'wed' ,'thurs' ,'fri','sat','sun']
print(days[day_of_week])
