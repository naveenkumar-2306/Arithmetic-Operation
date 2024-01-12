#Convert two lists into a dictionary
keys = []
values = []
n = int(input("Enter the number of items "))
d = {}
for i in range(n):
    kval = input("Enter the name of key")
    keys.append(kval)
    vval = int(input("Enter the value of the corresponding key"))
    values.append(vval)
print(keys)
print(values)
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)

