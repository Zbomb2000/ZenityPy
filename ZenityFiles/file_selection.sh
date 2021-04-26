#! /bin/bash

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

FILE_VAR=$(zenity --file-selection)

echo "$FILE_VAR" > "$SCRIPTPATH/text.txt"
