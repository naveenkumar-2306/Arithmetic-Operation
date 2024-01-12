ls = []
n = int(input("Enter the size of the list"))
print("Enter the list")
for i in range(n):
	a = int(input())
	ls.append(a)
if ls[0] == ls[n-1]:
	print("The first and last element are same")
else:
	print("The first and last element are not same")
