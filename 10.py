#Check file is empty or not
import os
file_name=input("Enter the filename:")
file_check=os.stat(file_name).st_size
if(file_check ==0):
   print("The file is empty")
else:
   print("The file is not empty")
