#!/bin/bash

#To check the file present in the directory or not

read -p "Enter the file name :  " filename

if [ -e "${filename}" ]
then 
	echo "File Presents"

	if [ -w "${filename}" ]
		then
			echo "File with Write Permission"
		else
			echo "File without Write Permission"
	fi

else
	echo "File doesn't Presents"
	exit 1
fi

