import sqlite3 as sql 

dbCon = sql.connect('Python Project Week 11/filmflix.db')

dbCursor = dbCon.cursor()