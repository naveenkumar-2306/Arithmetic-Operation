#!/bin/bash

# Exercise_8 - Write a script that executes the command “cat/etc/shadow”. If the command return a 0 exit status, report “command succeeded” and exit with a 0 exit status. If the command returns a non-zero exit status, report “Command failed” and exit with a 1 exit status.

# shadow file contains the hashed passphrase of the linux user accounts with properties related to the user password.
# this file is only  accessed by the root user, not by local host

# Storing the command in a variable comm
comm=$(cat /etc/shadow)

# Checking the status of the recently executed command
status=${?}

# If the status is true (0) then displaying the first the 2 line of the shadow file and reporting that command is executed successfully
if [[ ${status} -eq 0 ]]
then
	echo "Command succeeded"
	echo
	exit 0
else
	echo "Command failed"
	echo
	exit 1
fi
