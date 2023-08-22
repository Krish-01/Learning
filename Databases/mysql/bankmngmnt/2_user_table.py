# This table is for registration and login
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='MySQL123', database='bank')
cur = conn.cursor()
cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null)')
print('User table created')

"""In user_table we have username with primary key, it doesnt allow duplicate values.
Cannot register 2 users with same username."""
