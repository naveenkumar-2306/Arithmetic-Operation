	
#Change value of a key in a nested dictionary

d = {}
n = int(input("Enter te number of values in the dic"))
print("Enter the keys and value of dict:")
for i in range(n):
    key = input("Enter the key ")
    val = input("Enter the value ")
    d[key] = val

kval = input("Enter the value in which you want to check")
if kval in d.values():
	print("Hey, the given value does exist in the dict")
else:
	print("Sorry, given value doesn't exist in dict")

