#Find the day of the week of a given date

from datetime import datetime
date_input=input("Enter a date (YYYY-MM-DD): ")
given_date=datetime.strptime(date_input, "%Y-%m-%d")
day_of_week=given_date.weekday()
days_of_week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(f"The day of the week for {given_date} is {days_of_week[day_of_week]}")

