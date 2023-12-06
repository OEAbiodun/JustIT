import sqlite3 as sql 

# from sqlite3 import connect

dbCon = sql.connect('sqlite3DB/myUsers.db')

dbCursor = dbCon.cursor()