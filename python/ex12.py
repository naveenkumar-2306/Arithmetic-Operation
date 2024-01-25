# return array of odd rows and even columns 

import numpy

row = int(input('enter the number of rows: '))
col = int(input('enter the number of columns: '))

arr = []
print ('enter the elements rowwise:')

for i in range(row):
	a = []
	for j in range(col):
		a.append(int(input()))
	arr.append(a)
	
print(arr)

arr = numpy.array(arr)
	
new_arr = arr[1::2,::2]
print(new_arr)
