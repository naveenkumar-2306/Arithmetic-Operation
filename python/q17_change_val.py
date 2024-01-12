
#Change value of a key in a nested dictionary

d = {}
n = int(input("Enter te number of values in the dic"))
print("Enter the keys and value of dict:")
for i in range(n):
    key = input("Enter the key ")
    val = input("Enter the value ")
    d[key] = val

d1 ={}
m = int(input("Enter the number of keys"))
for i in range(m):
	kval = input("Enter the key")
	d1[kval] = d
print("\n\n",d1,"\n\n")

chekey = input("Enter the value of key to check whether the key is exist or not")
if chekey in d1.keys():
	print("Given key exist, enter the values")
	d2 = {}
	for i in range(n):
		key = input("Enter the key ")
		val = input("Enter the value ")
		d2[key] = val
	d1[chekey] = d2
	print(d1)
else:
	print("Sorry the given key is not available in")

