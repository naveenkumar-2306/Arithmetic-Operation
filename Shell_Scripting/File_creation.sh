#!/bin/bash

ls

n=10
name=test
para=.sh

#touch test${n}.sh


while [ $n -le 23 ]
do 
	touch test${n}.sh 
	chmod +777 ${name}${n}.sh 
	((n++))
done	


