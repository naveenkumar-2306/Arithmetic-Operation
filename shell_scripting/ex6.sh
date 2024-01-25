#!/bin/bash

for FILE in "${@}"
do

if [[ -f "${FILE}" ]]
then 
	echo 'this is a regular file'
elif [[ -d "${FILE}" ]]
then
	echo 'this file is a directory'
else
	echo 'this is another type of file'
fi

done
