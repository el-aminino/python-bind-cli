#!/bin/python3
#first import required libraries
import subprocess

def is_bind_installed():
    try:
        is_installed = subprocess.check_output("dpkg -s bind9")
        is_installed = is_installed.decode("utf8").lower()
        print(is_bind_installed)
    except:
        return False