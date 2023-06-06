#!/bin/python3

import subprocess
c = subprocess.getoutput("apt list --installed")
print("welcome to Bind9 editor")

if "bind9" not in c:
    bind_install = False
    print("Bind9 is not installed in this server please use command bellow as a privileged user \n")
    print("apt install bind9")

else :
    bind_install = True

if bind_install :
    print ("here is the zones in your configuration :")
