"""
python needs a MySQL Driver to access the mysql dtabase
"""
import mysql.connector

avDB=mysql.connector.connect(host="localhost", user="root", password="root")

print(avDB)