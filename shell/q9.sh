#!/bin/bash

# Exercise_9 - Write the shell script that renames all files in the current directory that end in “.jpg” to begin with today’s date in the following format: YYYY-MM-DD. For example, if a picture of my cat was in the current directory and today was October 31,2016 it would change name from “mycat.jpg” to “2016–10–31-mycat.jpg”.

# getting all the files ending jpg format
for image in *.jpg
do
	echo "${image}"
	newname="$(date +%F)-${image}"
	mv ${image} ${newname}
done

# Checking whether the filename has changed for not
for img in *.jpg
do
	echo "${img}"
done
