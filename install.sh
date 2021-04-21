#! /bin/bash

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

# This gives execution permission for the .sh scripts:
chmod +x "$SCRIPTPATH/ZenityFiles/warning.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/info.sh"
