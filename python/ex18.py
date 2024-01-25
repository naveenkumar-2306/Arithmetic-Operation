'''
create an outer function that will accept 2 parameter 
create a inner funtion that will calculate the a+b
outer function return the result by adding 5 to it
'''

def add5 (a,b):
	def add ():
		return a+b
	result = add()
	return result+5
	
n1 = int(input('enter n1:'))
n2 = int(input('enter n2:'))

ans = add5(n1,n2)

print(ans)

