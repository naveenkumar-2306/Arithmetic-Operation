#!/bin/bash
cat intro.txt

if [ ${?} -eq 0 ]
then
echo "Command success"
else
echo "Not success"
fi

