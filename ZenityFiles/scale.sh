#! /bin/bash

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

TEXT=$(cat "$SCRIPTPATH/text.txt")

SCALE_VAR=$(zenity --scale --text="$TEXT")

echo "$SCALE_VAR" > "$SCRIPTPATH/text.txt"
