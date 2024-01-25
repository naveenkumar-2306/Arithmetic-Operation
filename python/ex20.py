# recursive function to calculate the sum of numbers from 0 to 10

n = 10

def sum (n):
	if(n == 0):
		return 0
	return n + sum(n-1)
	
result = sum(n)
print(result)
