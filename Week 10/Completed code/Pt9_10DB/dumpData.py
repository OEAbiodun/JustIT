from connect import *

def dataDump():

    with open("Week 10\Completed code\Pt9_10DB\songs.sql") as songsData:
        insertScriptdata = songsData.read()

        dbCursor.executescript(insertScriptdata)

dataDump()