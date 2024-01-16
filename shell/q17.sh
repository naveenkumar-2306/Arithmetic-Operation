#!/bin/bash

# read write and excuetable

read -p "enter filename" name
ls -l ${name}
chmod 777 ${name}
ls -l ${name}

