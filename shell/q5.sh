#!/bin/bash

# write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file. Also perform an ls command against the file or directory with the long listing option.

# Getting the file or path from the user
echo "enter the file or path"
read nam

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

