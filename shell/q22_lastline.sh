#!/bin/bash

# last line of the file

read -p "enter the filename" name

tail -1 ${name}
