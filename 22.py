#Access value 20 from a tuple


tuple1 = ()
num = int(input("Enter the number of elements: "))
l = list(tuple1)

for i in range(0, num):
    var = int(input("Enter element: "))
    l.append(var)

tuple1 = tuple(l)

found = False
for i in range(0, num):
    if tuple1[i] == 20:
        found = True
        break

if found:
    print("Found 20")
else:
    print("Not found")



