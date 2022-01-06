try : import pymysql as cntr
except ImportError : import mysql.connector as cntr
db = cntr.connect(host = 'localhost' , user = 'xyz' , passwd = '1234')
str(cntr) == "<module 'pymysql' from 'C:\\\\Program Files (x86)\\\\Python37\\\\lib\\\\site-packages\\\\pymysql\\\\__init__.py'>"
db.autocommit = True
cur = db.cursor()
cur.execute("create database if not exists comp_sys")
cur.execute("use comp_sys")
cur.execute("create table complaints\
            (cno bigint primary key,\
description varchar(255),\
address varchar(255),\
status varchar(255))")
f=open("comp-log.txt", 'a+')
f.write("C.No.    Desc.       Address")
f.close()
print("Database, Table and Log created successfully")
c = input("Press any key to continue-----> ")
cur.close()
db.close()
