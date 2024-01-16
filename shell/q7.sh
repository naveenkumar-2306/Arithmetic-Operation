#!/bin/bash

# Exercise_7 - Write a shell script that displays, “This script will exit with 0 exit status.” Be sure that the script does indeed exit with a 0 exit status.

# displaying a command and checking its status and displaying it

echo "This script will exit with 0 exit status"
status=${?} # ${?} will return of the status of the most recent executed command in the script and the status in a variable

# Checking whether status of echo command is 0 or 1
if [[ ${status} -eq 0 ]]
then 
	echo "exit ${status}"
fi
# Making sure the script end with exit 0
exit 0
