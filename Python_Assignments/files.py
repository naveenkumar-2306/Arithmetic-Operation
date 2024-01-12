import os

file_name = input("Enter the name of the file :: ") # "file_new.txt"

while True:
    try:
        myfile = open(file_name,'r')
    except:
        file_name = input("Enter the name of the correctly")
        continue
    else:
        print("Thank you for the file name")
        break


file_access = myfile.readlines()
if (len(file_access) == 0):
    print("File is empty")

else:
    try:
        write_file = open("write_file.txt",'a')
    except:
        print("Unable to write into the file")

    line_number = int(input("Enter the line of the file need to skip :: "))
    for index,value in enumerate(file_access):
       if (index == line_number-1):
           pass
       else:
        write_file.write(value)
myfile.close()
write_file.close()


