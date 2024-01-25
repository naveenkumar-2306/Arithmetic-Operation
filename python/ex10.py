#Check file is empty or not

import os

file_name=input("Enter the filename:")

if(os.path.getsize(file_name) ==0):
   print("The file is empty")
else:
   print("The file is not empty")
