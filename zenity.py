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

def help():
    print("")
    print("zenity.info(TEXT) ; Replace 'TEXT' with the message you want to send. Same thing for 'error', 'warning', and 'question'.")
    print("")
