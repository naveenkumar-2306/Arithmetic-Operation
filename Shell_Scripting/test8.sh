#!/bin/bash

# Execute the command "cat/etc/shadow"

cat /etc/shadow 

echo "${?}"

if [ ! ${?} ]
then 
	echo "The command succeeded"
	exit 0
else
	echo "The command failed"
	exit 1
fi
