#!/bin/bash

read -p 'enter the file name: ' FILE

if [[ -f "${FILE}" ]]
then 
	echo 'this is a regular file'
elif [[ -d "${FILE}" ]]
then
	echo 'this file is a directory'
else
	echo 'this is another type of file'
fi

ls -l $FILE
