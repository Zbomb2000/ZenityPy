import subprocess
import os

cd = os.getcwd()

def warn():
    subprocess.Popen([cd + "/ZenityFiles/warning.sh"])
    print("hi")
    
