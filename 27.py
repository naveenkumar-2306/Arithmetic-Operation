#Subtract a week (7 days)  from a given date in Python

from datetime import datetime,timedelta
given_date=input("Enter the date (YYYY-MM-DD):")
date_input=datetime.strptime(given_date,"%Y-%M-%d")
result= date_input-timedelta(days=7)
print(result)

