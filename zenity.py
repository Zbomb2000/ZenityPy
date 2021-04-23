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
