#!/bin/bash

# process name with process id

read -p "enter the process id" proid

ps -p ${proid} -o comm=
