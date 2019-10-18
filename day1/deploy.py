import pymysql
import function
import sys


db = pymysql.connect("localhost","root","1234QWER","TESTDB" )

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print ("Database version : %s " % data)




