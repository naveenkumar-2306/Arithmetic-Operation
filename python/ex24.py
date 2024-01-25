# count the repeated number in the tuple

original = []

n = int(input('enter the number of elements:'))

print('enter the elements:')
for i in range(n):
	a = int(input())
	original.append(a)
	
original = tuple(original)

myset = set(original)

repeat = {}
for i in myset:
	count = original.count(i)
	count = str(count)
	sen = 'repeated ' + count + ' times'
	repeat[i] = sen
	
print(repeat)
