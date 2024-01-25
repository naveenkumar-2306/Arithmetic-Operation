# subtract a week (7 days ) from a given date 

from datetime import datetime , timedelta

print ("current time: ", datetime.now())

print(datetime.now() + timedelta(days = -7))

