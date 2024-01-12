# Write all content of a given file into a new file by skipping line number 5
with open("e1.txt",'r') as f1:
	contents = f1.readlines()
for cont in contents:
	print(cont)
n = int(input("Which line do you want to skip"))

with open("e2.txt",'w') as f2:
	count = 1;
	for content in contents:
		if count == n:
			count = count +1
			continue
			
		else:
			f2.write(content)
			count = count+1

with open("e2.txt",'r') as f3:
	for line in f3.readlines():
		print(line)
	
