from connect import *

def read_songs():
    
    dbCursor.execute("SELECT * FROM songs")
    allRecords = dbCursor.fetchall()

    for eachRecords in allRecords:
        print(eachRecords)

if __name__ == "__main__":
    read_songs()