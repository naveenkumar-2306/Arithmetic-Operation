#Return array of odd rows and even columns from below numpy array

import numpy as np
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of columns:"))
user_array=np.empty((rows,cols),dtype=int)
for i in range(rows):
  for j in range(cols):
     user_array[i,j]=int(input(f"Enter element at position ({i+1},{j+1}):"))
  
  
print(user_array)
odd_even=user_array[::2,1::2]
print("Array of odd rows and even columns:")
print(odd_even)

