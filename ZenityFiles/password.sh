#! /bin/bash

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

PASSWORD_VAR=$(zenity --password)

echo "$PASSWORD_VAR" > "$SCRIPTPATH/text.txt"
