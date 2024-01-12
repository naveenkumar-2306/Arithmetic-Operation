#convert the string into date
#this can be done using strptime() from datetime module. the ysyntax is given the str and the clock format of the given str and the str will be converted into time object
from datetime import datetime

str1 = input("Enter the date and time in 'day-month-year' and 'hour:min:sec' format")
print(str1)
cstr = datetime.strptime(str1, '%d/%m/%Y %H:%M:%S')
print(cstr)
print(type(cstr))
