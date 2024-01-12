#!/bin/bash

for file_name in "$@"
do
	if [ -e $file_name ]
	then
		echo "The file $file_name is exists"
	else
		echo "The file $file_name doesn't exists"
	fi
done
