#! /bin/bash

TEXT=$(cat '/mnt/chromeos/MyFiles/ZenityPy/ZenityFiles/text.txt')

zenity --warning \
--text="$TEXT"
