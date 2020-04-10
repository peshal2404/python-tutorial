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

###MySQL###

import mysql.connector

from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='scott',
                                database='employ')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()