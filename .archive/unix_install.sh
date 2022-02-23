#! /bin/bash

sudo apt install zenity

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")

dos2unix "$DIR/ZenityFiles/warning.sh"
dos2unix "$DIR/ZenityFiles/error.sh"
dos2unix "$DIR/ZenityFiles/info.sh"
dos2unix "$DIR/ZenityFiles/question.sh"
dos2unix "$DIR/ZenityFiles/password.sh"
dos2unix "$DIR/ZenityFiles/color_selection.sh"
dos2unix "$DIR/ZenityFiles/file_selection.sh"
dos2unix "$DIR/ZenityFiles/notification.sh"
dos2unix "$DIR/ZenityFiles/scale.sh"
dos2unix "$DIR/ZenityFiles/entry.sh"
dos2unix "$DIR/ZenityFiles/calendar.sh"

echo "Done!"
