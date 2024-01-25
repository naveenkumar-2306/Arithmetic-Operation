#!/bin/bash

if [[ -f file_path ]]
then
	echo ' file_path passwords are enabled'
fi
if [[ -w file_path ]]
then
	echo 'you have permission to edit "file_path" '
else
	echo 'you do not have permission to edit "file_path" '
fi
    
