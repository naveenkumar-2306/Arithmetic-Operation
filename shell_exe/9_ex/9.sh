#Exercise_9 - Write the shell script that renames all files in the current directory that end in “.jpg” to begin with today’s date in the following format: YYYY-MM-DD. For example, if a picture of my cat was in the current directory and today was October 31,2016 it would change name from “mycat.jpg” to “2016–10–31-mycat.jpg”.


#!/bin/bash
today=$(date +"%Y-%m-%d")
for file in *.jpg; do
    if [ -f "$file" ]; then
        extension="${file##*.}"
        new_name="${today}-${file}"
        mv "$file" "$new_name"
        echo "Renamed: $file to $new_name"
    fi
done

