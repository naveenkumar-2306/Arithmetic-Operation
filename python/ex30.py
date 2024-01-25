# calculate number of days between two given dates

import datetime 

date1 = (input('enter dd/mm/yyyy :'))
date2 = (input('enter dd/mm/yyyy :'))

date1 = datetime.datetime.strptime(date1, '%d/%m/%Y')
date2 = datetime.datetime.strptime(date2, '%d/%m/%Y')

if date2 > date1:
	print((date2-date1).days)
else:
	print((date1-date2).days)

