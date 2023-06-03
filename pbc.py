#!/bin/python3

import subprocess
c = subprocess.getoutput("apt list --installed")
print("welcome to Bind9 editor")

if "bind9" not in c:
    print("Bind9 is not installed in this server please use command bellow as a privileged user \n")
    print("apt install bind9")

