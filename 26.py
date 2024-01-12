#Convert string into a datetime object

from datetime import datetime

datetime_str=input("Enter a string:")


datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S')
print(datetime_object) 
