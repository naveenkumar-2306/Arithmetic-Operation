# sort the tuple of tuple by 2nd item

original = []

n = int(input('enter the number of elements:'))

print('enter the elements:')
i = 0
for i in range(n):
	b = []
	a = (input('enter a character:'))
	b.append(a)
	num = int(input('enter a number:'))
	b.append(num)
	b = tuple(b)
	original.append(b)
		
	
original = tuple(original)
print(original)

original = tuple(sorted(list(original), key = lambda x : x[1]))
print(original)
