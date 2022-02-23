#! /bin/bash

sudo apt install zenity

# This gets the file location of the script:
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

# This gives execution permission for the .sh scripts:
chmod +x "$SCRIPTPATH/ZenityFiles/warning.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/info.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/question.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/error.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/password.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/color_selection.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/file_selection.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/notification.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/scale.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/entry.sh"
chmod +x "$SCRIPTPATH/ZenityFiles/calendar.sh"

echo "Done!"
