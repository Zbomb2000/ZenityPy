# ZenityPy

Zenity support for Python on Linux


## Modules
The only current module is the main zenity module.
- ```from ZenityPy import zenity```

## Setup

Run the "install" file:
- Change the directory to the main package file
- Type ```chmod +x install.sh```
- Type: ```./install.sh```.
The package should then be set up.

## Functions
- ```zenity.info("TEXT")``` This sends a message box. Replace TEXT with the message you want to send with the warning (Also used with ```zenity.question()```, ```zenity.error()```, and ```zenity.warning()```).
- ```zenity.password()``` This creates a password messege box. This returns a string.
- ```zenity.color_selection()``` This creates a color selection messege box. This returns an rgb value.
- ```zenity.file_selection()``` This creates a file selection messege box. This returns a file path.
- ```zenity.entry("TEXT")``` This sends a text box the user can fill in input. Replace text with the message that you want to send with the text box.
- ```zenity.notification("TEXT")``` This sends a notification. Replace text with the message that you want to send with the notification.
- ```zenity.calendar("TEXT")``` This sends a calendar that the user can pick a day from. Replace text with the message that you want to send with the calendar. This returns a date (10/2/2018).
- ```zenity.scale("TEXT")``` This sends a message box that a number from 0-100 can be chosen. Replace text with the message that you want to send with the message box. This returns and int value from 0-100.
