#Add a week (7 days) and 12 hours to a given date

from datetime import datetime,timedelta
date_input=input("Enter a date and time (YYYY-MM-DD HH:MM:SS):")
given_date=datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
result_date=given_date+timedelta(days=7,hours=12)
print("Original date and time:",given_date)
print("Result after adding a week and 12 hours:",result_date)
