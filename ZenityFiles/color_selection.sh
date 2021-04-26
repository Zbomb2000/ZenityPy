#! /bin/bash

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

RGB_VAR=$(zenity --color-selection)

echo "$RGB_VAR" > "$SCRIPTPATH/text.txt"
