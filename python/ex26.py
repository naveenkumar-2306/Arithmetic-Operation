# convert string into datetime object

import datetime

datetime_str=input("Enter a string in this format '%d/%m/%Y %H:%M':")


datetime_object = datetime.datetime.strptime(datetime_str, '%d/%m/%Y %H:%M')
print(datetime_object) 
