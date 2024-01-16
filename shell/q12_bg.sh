#!/bin/bash

# running file in background

if [[ ${#} -ne 1 ]]
then
	echo "please provide 1 argument"
	exit 1
fi
nohup ${1} &
echo "jobs -l"
jobs -l
read -p "Do you want to kill the process (Y/N)" stat
if [[ stat -eq 'y' || stat -eq 'Y' ]]
then
	read -p "input the process id" id
	kill ${id}
fi

