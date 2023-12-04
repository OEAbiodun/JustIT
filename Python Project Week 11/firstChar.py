from connect import *
from tabulate import tabulate

def firstChar():

    inputCharact = input("Enter the first character of a movie: ").capitalize()
    
    # dbCursor.execute("SELECT * FROM tblFilms WHERE Genre = {};".format(inputGenre))
    dbCursor.execute("SELECT * FROM tblFilms WHERE title LIKE ?",(inputCharact +'%', ))
    allRecords = dbCursor.fetchall()

    # for charact in allRecords:
    #     print(charact)

    if allRecords:
        headers = [i[0] for i in dbCursor.description]
        table = tabulate(allRecords, headers, tablefmt="grid")
        # print("Total number of rows in table: ", dbCursor.rowcount)
        print(table)
    else:
        print("No data found.")

if __name__ == "__main__":
    firstChar()