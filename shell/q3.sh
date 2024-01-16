#!/bin/bash

# Exercise_3 - Store the output of the command “hostname” in a variable. Display “This script is running on _.” where “_” is the output of the “hostname” command.

# HOSTNAME is a built-in shell command where it automatically set the name of the current host

hostname=$(hostname)
echo "this scirpt is running on ${hostname}"

