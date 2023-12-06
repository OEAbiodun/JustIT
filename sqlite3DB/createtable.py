from connect1 import * # import the connect.py module 

dbCursor.execute(""" 
CREATE TABLE IF NOT EXISTS "users" (
    "MemberID"  INTEGER NOT NULL UNIQUE,
    "username" TEXT,
    "Email" TEXT,
    PRIMARY KEY("MemberID" AUTOINCREMENT)
)""")
