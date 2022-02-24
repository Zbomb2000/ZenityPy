#!/usr/bin/python3
import subprocess

def password():
    pw_input = subprocess.check_output(['zenity', '--password'])
    pw1 = pw_input.decode("utf-8")
    pw2 = pw1[:len(pw1) - 1]
    return pw2

def warning(*args, **kwargs):
    text1 = kwargs.get('text', "Are you sure you want to proceed?")
    pw_input = subprocess.check_output(['zenity', '--warning', '--text='+str(text1)])

def info(*args, **kwargs):
    text1 = kwargs.get('text', "All updates are complete.")
    info_input = subprocess.check_output(['zenity', '--info', '--text='+str(text1)])

def question(*args, **kwargs):
    text1 = kwargs.get('text', "Are you sure you want to proceed?")
    question_input = subprocess.check_output(['zenity', '--question', '--text='+str(text1)])

def error(*args, **kwargs):
    text1 = kwargs.get('text', "An error has occurred.")
    error_input = subprocess.check_output(['zenity', '--error', '--text='+str(text1)])
