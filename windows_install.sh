#! /bin/bash

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")

dos2unix "$DIR/ZenityFiles/warning.sh"
dos2unix "$DIR/ZenityFiles/error.sh"
dos2unix "$DIR/ZenityFiles/info.sh"
dos2unix "$DIR/ZenityFiles/question.sh"
dos2unix "$DIR/ZenityFiles/password.sh"

echo "Done!"
