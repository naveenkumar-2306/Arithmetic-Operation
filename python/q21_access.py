#Access value ‘20’ from a tuple.
tup = ()
l = list(tup)
n = int(input("Enter the number of elements in the tuple"))
for i in range(n):
	ele = input("enter the element")
	l.append(ele)
tup = tuple(l)
num = input("Enter the element to accessed form the tuple")
if num in tup:
	i = tup.index(num)
	print(f"the element is present and accessed at location {i+1}")
else:
	print("Sorry given element is not present in the tuple")
