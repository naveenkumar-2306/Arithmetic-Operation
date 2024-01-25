# reverse a tuple

original = []

n = int(input('enter the number of elements:'))

print('enter the elements:')
for i in range(n):
	a = int(input())
	original.append(a)
	
original = tuple(original)
reverse = original[::-1]
print(reverse)
