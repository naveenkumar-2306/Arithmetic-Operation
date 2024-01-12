#Return array of odd rows and even columns from below numpy array

import numpy as np

arr1 = np.array([[1,2,3,4,5],[2,3,4,5,6], [12,13,14,15,16],[23,34,45,56,66]])

arr2 = arr1[::2,1::2]
print(arr1)
print(arr2)
