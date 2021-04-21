#! /bin/bash

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

TEXT=$(cat "$SCRIPTPATH/text.txt")

zenity --warning \
--text="$TEXT"
