import subprocess
import os

cd = os.path.realpath('ZenityPy')

def warning(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/warning.sh"])

def info(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/info.sh"])

def question(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/question.sh"])

def error(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/error.sh"])

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

def help():
    print("")
    print("zenity.info(TEXT) ; Replace 'TEXT' with the message you want to send. Same thing for 'error', 'warning', and 'question'.")
    print("")
