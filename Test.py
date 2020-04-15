#!/usr/bin/python
## Written by Peshal Oli
import mysql.connector
import json
import os
import subprocess
import requests
import sys
# response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
# print(response.status_code)
# response = requests.get("http://api.open-notify.org/astros.json")
# print(response.status_code)
# print(response.json())
# f = os.popen('date')
# now = f.read()
# print ("Today is ", now)
# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
# jprint(response.json())
#subprocess.call(["cat", "/etc/resolv.conf"])
###MySQL###
# import mysql.connector
# from mysql.connector import errorcode
# try:
#   cnx = mysql.connector.connect(user='scott',
#                                 database='employ')
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()

#Home_Dir = /Users/peshal/Downloads
subprocess.call(["ls", "-l", "/Users/peshal/Downloads/"])

##For API
import urllib
import json





