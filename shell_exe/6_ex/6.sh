#Exercise_6 - Modify the previous script to accept an unlimited number of files and directories as arguments

#!/bin/bash
for name in "$@"; do
if [ -e "$name" ];
then
  if [ -f  "$name" ];
  then 
    echo "It is a regular file"
  elif [ -d "$name" ];
  then
    echo "It is a directory"
  elif [ -c "$name" ];
  then
    echo "It is a character file"
  elif [ -b "$name" ];
  then
    echo "It is a binary file"
  else
    echo "It is another type of file"
  fi
ls -l "$name"
 else
 echo "File not exists"
fi
done
