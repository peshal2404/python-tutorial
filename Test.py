#!/usr/bin/python
import mysql.connector
import os
import subprocess
import sys

#subprocess.call("date")

f = os.popen('date')
now = f.read()
print ("Today is ", now)
##subprocess.call(["cat", "/etc/resolv.conf"])

cmdping = "ping -c2 peshal.com.np"
p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
         sys.stdout.write(out)
         sys.stdout.flush()
