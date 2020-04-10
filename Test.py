#!/usr/bin/python
import mysql.connector
import os
import subprocess
import sys

#subprocess.call("date")

f = os.popen('date')
now = f.read()
print ("Today is ", now)
subprocess.call(["cat", "/etc/resolv.conf"])

