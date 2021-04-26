# ZenityPy

Zenity support for Python on Linux

- from ZenityPy import zenity

## Setup

Run the "install" file:
- Change the directory to the main package file
- Type ```chmod +x install.sh```
- Type: ```./install.sh```.
The package should then be set up.

## Functions
- ```zenity.info("TEXT")``` This sends a message box. Replace TEXT with the message you want to send with the warning (Also used with ```zenity.question()```, ```zenity.error()```, and ```zenity.warning()```).
- ```zenity.password()``` This creates a password messege box. You can use it this way: ```random_var = zenity.password()```.
