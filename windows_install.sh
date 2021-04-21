#! /bin/bash

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")

dos2unix "$DIR/ZenityFiles/warning.sh"
echo "Done!"
