import subprocess
import os

cd = os.path.realpath('ZenityPy')

def warning(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/warning.sh"])
    return text

def info(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/info.sh"])
    return text

def question(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/question.sh"])
    return text

def error(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/error.sh"])
    return text

def password():
    subprocess.Popen([cd+"/ZenityFiles/password.sh"])
    f = open(cd+"/ZenityFiles/text.txt", "r")
    wait_var1 = f.read()
    while (True):
        f = open(cd+"/ZenityFiles/text.txt", "r")
        wait_var = f.read()
        if wait_var != wait_var1:
            break
    f = open(cd+"/ZenityFiles/text.txt", "r")
    password_var = f.read()
    f.close()
    size = len(password_var)
    return password_var[:size - 1]

def color_selection():
    subprocess.Popen([cd+"/ZenityFiles/color_selection.sh"])
    f = open(cd+"/ZenityFiles/text.txt", "r")
    wait_var1 = f.read()
    while (True):
        f = open(cd+"/ZenityFiles/text.txt", "r")
        wait_var = f.read()
        if wait_var != wait_var1:
            break
    f = open(cd+"/ZenityFiles/text.txt", "r")
    rgb_var = f.read()
    f.close()
    size = len(rgb_var)
    return rgb_var[:size - 1]

def file_selection():
    subprocess.Popen([cd+"/ZenityFiles/file_selection.sh"])
    f = open(cd+"/ZenityFiles/text.txt", "r")
    wait_var1 = f.read()
    while (True):
        f = open(cd+"/ZenityFiles/text.txt", "r")
        wait_var = f.read()
        if wait_var != wait_var1:
            break
    f = open(cd+"/ZenityFiles/text.txt", "r")
    file_path_var = f.read()
    f.close()
    size = len(file_path_var)
    return file_path_var[:size - 1]

def notification(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(text)
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/notification.sh"])
    return text

def scale(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/scale.sh"])
    f = open(cd+"/ZenityFiles/text.txt", "r")
    wait_var1 = f.read()
    while (True):
        f = open(cd+"/ZenityFiles/text.txt", "r")
        wait_var = f.read()
        if wait_var != wait_var1:
            break
    f = open(cd+"/ZenityFiles/text.txt", "r")
    scale_var = f.read()
    f.close()
    size = len(scale_var)
    return scale_var[:size - 1]

def entry(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/entry.sh"])
    f = open(cd+"/ZenityFiles/text.txt", "r")
    wait_var1 = f.read()
    while (True):
        f = open(cd+"/ZenityFiles/text.txt", "r")
        wait_var = f.read()
        if wait_var != wait_var1:
            break
    f = open(cd+"/ZenityFiles/text.txt", "r")
    entry_var = f.read()
    f.close()
    size = len(entry_var)
    return entry_var[:size - 1]

def calendar(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/calendar.sh"])
    f = open(cd+"/ZenityFiles/text.txt", "r")
    wait_var1 = f.read()
    while (True):
        f = open(cd+"/ZenityFiles/text.txt", "r")
        wait_var = f.read()
        if wait_var != wait_var1:
            break
    f = open(cd+"/ZenityFiles/text.txt", "r")
    calendar_var = f.read()
    f.close()
    size = len(calendar_var)
    return calendar_var[:size - 1]

def help():
    print("")
    print("zenity.info(TEXT) ; Replace 'TEXT' with the message you want to send. Same thing for 'error', 'warning', and 'question'.")
    print("zenity.password() This creates a password messege box. This returns a string.")
    print("zenity.color_selection() This creates a color selection messege box. This returns an rgb value.")
    print("zenity.file_selection() This creates a file selection messege box. This returns a file path.")
    print("zenity.entry(TEXT) This sends a text box the user can fill in input. Replace text with the message that you want to send with the text box.")
    print("zenity.notification(TEXT) This sends a notification. Replace text with the message that you want to send with the notification.")
    print("zenity.scale(TEXT) This sends a message box that a number from 0-100 can be chosen. Replace text with the message that you want to send with the message box. This returns and int value from 0-100.")
    print("zenity.calendar(TEXT) This sends a calendar that the user can pick a day from. Replace text with the message that you want to send with the calendar. This returns a date (10/2/2018).")
    print("")
    
