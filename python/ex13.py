# delete the sencond column and insert the new column

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

arr = numpy.array(arr)
print(arr)

arr = numpy.delete(arr,1,1)
print(arr)

new_col = []
print ('enter the new column:')
for i in range(col):
	new_col.append(int(input()))

new_arr = numpy.insert(arr, 1, new_col,axis=1)

print(new_arr)	
