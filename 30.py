#Calculate number of days between two given dates

from datetime import datetime
start_date_input=input("Enter start date (YYYY-MM-DD):")
end_date_input=input("Enter end date (YYYY-MM-DD):")
start_date=datetime.strptime(start_date_input,"%Y-%m-%d")
end_date=datetime.strptime(end_date_input,"%Y-%m-%d")
days_diff=(end_date-start_date).days
print(f"The number of days between {start_date} and {end_date} is {days_diff} days")

