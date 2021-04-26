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
