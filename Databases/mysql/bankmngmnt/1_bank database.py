import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='MySQL123', use_pure=True)
# if conn.is_connected():
# print('connected successfully')

cur = conn.cursor()
cur.execute('create database bank')
print('Bank database created successfully')
