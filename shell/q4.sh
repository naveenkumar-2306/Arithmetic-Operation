#!/bin/bash

# Exercise_4 - Write a shell script to check to see if the file “file_path” exists. If it does exist, display “file_path passwords are enabled.” Next, check to see if you can write to the file. If you can, display “You have permissions to edit “file_path.””If you cannot, display “You do NOT have permissions to edit “file_path””

path=file_path.txt

if [ -f "${path}" ]
then
	echo "file_path passwords are enabled"
else 
	echo "file_path passwords are not enabled"
fi

if [ -w "${path}" ]
then
	echo "You have permissions to edit ${path}."
else 
	echo "You do NOT have permissions to edit ${path}."
fi

