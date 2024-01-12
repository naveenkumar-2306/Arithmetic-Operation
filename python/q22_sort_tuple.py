#sort the tuple based upon the values
tup = ()
l = list(tup)
n = int(input("Enter the number of elements in the tuple"))
for i in range(n):
	e1 = input("enter the item 1")
	e2 = int(input("enter the item 2"))
	tup1 = (e1,e2)
	l.append(tup1)
tup = tuple(l)
print(tup)
l.sort(key = lambda x:x[1])
tup = tuple(l)
print(tup)
