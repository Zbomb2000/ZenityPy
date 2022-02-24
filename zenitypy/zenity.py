#!/usr/bin/python3
import subprocess

def password():
    pw_input = subprocess.check_output(['zenity', '--password'])
    pw1 = pw_input.decode("utf-8")
    pw2 = pw1[:len(pw1) - 1]
    return pw2
