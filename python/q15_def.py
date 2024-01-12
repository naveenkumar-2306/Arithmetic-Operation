ls = []
d1 = {}
print("Enter default value:")
choice = 1
while(choice == 1):
    print("enter the key and value")
    key = input("key: ")
    val = input("value: ")
    d1[key] = val
    c = input("Do you want to add another value (y/n)")
    if c == 'y' or c == 'Y':
        choice = 1
    else:
        choice = 0
n = int(input("Enter the number of employees"))
for i in range(n):
    name = input("Enter the name of the employee")
    ls.append(name)
    
d = {}
for i in range(n):
    d[ls[i]] = d1
print(d)

