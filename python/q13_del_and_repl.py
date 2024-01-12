#Delet 2nd column and replace

import numpy as np
ls = []
arr = np.array([])
m = int(input("Enter the no of rows of the aray"))
n = int(input("Enter the no of columns of the aray"))
for i in range(m):
    for j in range(n):
        num = int(input(f"enter number for row{i+1}: "))
        ls.append(num)
        lsarr = np.array(ls)
    arr = np.insert(arr,i,lsarr,axis = 0)#insert(arrname,value of ojbect, item to be inserted, axis will determine row or column, 0 means row, 1 means column
    ls.clear()
arr = arr.reshape(m,n)
print(arr,"\n")
col = int(input("Enter the value of the column to bee delted"))
print(f"the array after deleting column {col}:\n")
arr = np.delete(arr,col-1,axis = 1)
print(arr)
print("\n")
print("Enter the new values for replacment")
for i in range(m):
    n = int(input())
    ls.append(n)
lsarr = np.array(ls)
arr = np.insert(arr,col-1,lsarr,axis = 1)
print("\nThe new array after replacement is :")
print(arr)


