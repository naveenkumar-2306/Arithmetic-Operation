#!/bin/bash

DATE=$(date +%F)

echo "${DATE}"

for file in *.jpeg 
do
	base_name=$(basename "$file" .jpeg)
	
	new_name="${DATE}${base_name}.jpeg"
	
	mv "$file" "$new_name"
done
