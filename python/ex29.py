# add a week and 12 hours to a given date

from datetime import datetime , timedelta

print ("current time: ", datetime.now())

print(datetime.now() + timedelta(days = 7,hours = 12))

