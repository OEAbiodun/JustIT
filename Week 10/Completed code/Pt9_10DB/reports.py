from connect import * 

def reports():
    dbCursor.execute("SELECT Artist, Title FROM songs ORDER BY Artist DESC")
    dbCursor.execute("SELECT * FROM songs WHERE Genre = 'rock' OR 'pop' ")
    # dbCursor.execute("SELECT")

    reportsDaa = dbCursor.fetchall()

    for records in reportsDaa:
        print(records)

if __name__ == "__main__":
    reports()
