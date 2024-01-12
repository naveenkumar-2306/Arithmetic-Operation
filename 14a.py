#Delete the second column from a given array and insert the following new column in its place.   Array:   [[34,43,73],[82,22,12],[53,94,66]]   New arr: [[10,10,10]]


import numpy as np
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of columns:"))
array=np.empty((rows,cols),dtype=int)
for i in range(rows):
  for j in range(cols):
     array[i,j]=int(input(f"Enter element at position ({i+1},{j+1})"))
     
print("Array")
print(array)

new_col=np.array([int(input(f"Enter new element for col at pos {i+1}:")) for i in range (rows)])
array=np.delete(array,1,axis=1)
array=np.insert(array,1,new_col,axis=1)
print("Array after deleting the second column ");
print(array)

