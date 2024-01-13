#!/bin/bash

echo "Below is the output of for loop"
echo
for i in {1..3}
do
echo "Hi"
done

echo "============================================"

echo "Below is the output of while loop"
echo
count=1
while [ $count -le 3 ]
do
echo "Hello"
((count++))
done


echo "============================================="


echo "Below is the output of until loop"
echo 
count2=1
until [ $count2 -gt 3 ]
do
echo "Keerthanaporkodi"
((count2++))
done

