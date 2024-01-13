#Exercise_3 - Store the output of the command “hostname” in a variable. Display “This script is running on _.” where “_” is the output of the “hostname” command.

#!/bin/bash
NAME=$(hostname)
echo "This script is running on $NAME"
