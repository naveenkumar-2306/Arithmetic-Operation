# Counts the repeated number in the tuple.

d = {}
tup = ()
l = []
n = int(input("Enter the number of element"))
for i in range(n):
	num = int(input("enter the number:"))
	l.append(num)
for i in l:
	if i in d.keys():
		d[i] += 1
	else:
		d[i] = 1
print(f"element   count")
for i in d.keys():
	print(f"{i}   \t {d[i]}")	
