import numpy as np

arr = np.array([[100,110],[120,130],[140,150],[160,170],[180,190]])
for i in range(len(arr)):
    if(i % 2 == 0):
        print(arr[i][1])



#Dynamic 


rows = int(input("Enter the size of array of rows ::"))
cols = int(input("Enter the size of array of columns ::"))
arr =[]

for i in range(rows):
	col = []
	for j in range(cols):
		col.append((int(input("Enter the number one by one :: "))))
	arr.append(col)
	
for i in range(len(arr)):
    if(i % 2 == 0):
        print(arr[i][1])

print(arr)






##Deleting the second column and insert the new column

print("\n")
new_arr = np.delete(arr,1,0)  ## (array_name, row or column ,axis) axis 0 = row , axis 1 = column
print(new_arr)
print("\n")
arr_insert = [4,5,6]
arr_insert = np.insert(new_arr,1,arr_insert,0)
print(arr_insert)





##  https://numpy.org/doc/stable/user/absolute_beginners.html
