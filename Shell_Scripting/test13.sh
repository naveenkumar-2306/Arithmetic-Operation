#/bin/bash

## while loop
n=1
while [ $n -le 10 ]
do
	echo " Number in while : $n"
	((n++))
done

## for loop

for var in {1..10} 
do
	echo "For loop execute : Hello"
done

## until loop

a=1
until [ $a -ge 10 ]
do
	echo " Until Loop : $a"
	((a++))
done	


