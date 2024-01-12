#Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b. At last, an outer function will add 5 into addition and return it
def outfunc(a,b):
	def innfunc(a,b):
		a = a+b
		return a
	res = innfunc(a,b) + 5
	return res

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
result = outfunc(n1,n2)
print("\nThe result is: ",result) 
	
