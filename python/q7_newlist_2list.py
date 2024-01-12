l1 = [1,2,3,4,5,6,7,8,9,0]
l2 = [11,12,13,14,15,16,17,18,19,10,13]
l3 = []

for i in l1:
	if i%2 == 0:
		l3.append(i)
for i in l2:
	if i%2 != 0:
		l3.append(i)

print(f"The new list is\n{l3}") 
