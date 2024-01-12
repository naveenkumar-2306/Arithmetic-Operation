# Cheking file is empty of not
import os
print(os.name)
fil = input("Please enter the filename: ")
fileex = os.path.getsize(fil)

if fileex == 0:
    print("The file is empty")
else:
    print("The file is not empty")
    choice = input("Do you want to see teh content of the file?(y/n) ")
if choice == 'y' or choice == 'Y':
    with open(fil,'r') as f1:
        conts = f1.readlines()
        for cont in conts:
            print(cont)
        
