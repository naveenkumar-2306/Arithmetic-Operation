#Exercise_5 - write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file. Also perform an ls command against the file or directory with the long listing option.

read -p "Enter file name or directory:" name
if [ -e $name ]
then
  if [ -f  $name ]
  then 
    echo "It is a regular file"
  elif [ -d $name ]
  then
    echo "It is a directory"
  elif [ -c $name ]
  then
    echo "It is a character file"
  elif [ -b $name ]
  then
    echo "It is a binary file"
  else
    echo "It is another type of file"
  fi
ls -l $name
 else
 echo "File not exists"
fi


