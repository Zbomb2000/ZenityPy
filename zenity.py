import subprocess
import os

cd = os.path.realpath('ZenityPy')
# /mnt/chromeos/MyFiles/ZenityPy/

def warning(text):
    f = open(cd+"/ZenityFiles/text.txt", "w")
    f.write(str(text))
    f.close()
    subprocess.Popen([cd+"/ZenityFiles/warning.sh"])
