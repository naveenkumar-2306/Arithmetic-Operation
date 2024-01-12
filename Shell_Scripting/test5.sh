#!/bin/bash

#Prompts the user for name of a file

echo -e "Enter the name of the file : \c "

read file_name

# Directory as input:: /home/mahesh/Desktop/Learning/Shell_Scripting/(file_name)

if [ -e $file_name ] 
then
	echo " The file exists "
	if [ -f $file_name ]
	then
		echo " It is a regular file "
	fi

	if [ -d $file_name ]
	then
		echo " Directory present "
	fi

else
	echo " The file doesn't exists "
fi

ls -al
