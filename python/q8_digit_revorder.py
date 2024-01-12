# Write a Program to extract each digit from an integer in the reverse order.
num = int(input("Enter an integer"))
ls = []
newnum = 0
while(num > 0):
	n = int(num%10)
	newnum = (newnum*10) + n
	ls.append(n)
	num = int(num/10)
	
print(f"The reversed integer is {newnum}\nThe list is: {ls}")
