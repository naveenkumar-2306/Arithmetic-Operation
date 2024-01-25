# access value '20' from a tuple

original = []

n = int(input('enter the number of elements:'))

print('enter the elements:')
for i in range(n):
	a = int(input())
	original.append(a)
	
original = tuple(original)

value = 20

flag = 0

for i in range(n):
	if original[i] == 20:
		print(f'value found at {i}')
		flag = 1
if flag == 0:
	print('value not found')
	
		
