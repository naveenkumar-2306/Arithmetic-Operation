#!/bin/bash

# For loop
echo "For loop"
i='0'
for i in 21,33,44,51 
do
  echo "${i}"
done

# while loop
echo
echo "while loop"
x=7
while [[ "$x" -gt 4 ]]
do
	echo $x
	x=$(("$x"-1))
done
