# check if a value exists in a dictionary

n = int(input('enter the number of elements: '))

dictionary = {}

for i in range (n):
	key = input('enter the key:')
	value = input('enter the value:')
	dictionary[key] = value
	
search = input('enter the value to be searched:')


if search in dictionary.values() :
	print(' value exists ')
else:
	print(" value doesn't exist ")
	

