#!/bin/bash

# Exercise_6 - Modify the previous script (check whether reglar file, directory or another type of file) to accept an unlimited number of files and directories as arguments.

# Checking whether theuser has given any arguments
if [[ ${#} -lt 1 ]]
then
	echo "Please enter arguments"
	exit 1
fi
# Assigning the all the arguments to variable files
files="${@}"
# using for loop to check each argument and display the long list
for nam in ${files}
do
	# Checking the given argument is regular file, any type of file or directory
	if [[ -f ${nam} ]]
	then
		echo "This is a regular file"
	elif [[ -d ${nam} ]]
	then 
		echo "This is a directory"
	else [[ -e ${nam} ]]
		echo "This is an another type of file"
	fi

	# Long listing of the file or the directory
	ls -l ${nam}
	echo
done
