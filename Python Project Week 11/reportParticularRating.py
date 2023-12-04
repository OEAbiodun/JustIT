from connect import *
from tabulate import tabulate

def report_rating():

    reportRating = input("Enter the Movie Rate: ").upper()
    
    # dbCursor.execute("SELECT * FROM tblFilms WHERE Genre = {};".format(inputGenre))
    dbCursor.execute("SELECT * FROM tblFilms WHERE rating = ?", (reportRating, ))
    allRecords = dbCursor.fetchall()

    # for eachRecords in allRecords:
    #     print(eachRecords)

    if allRecords:
        headers = [i[0] for i in dbCursor.description]
        table = tabulate(allRecords, headers, tablefmt="grid")
        print(table)
    else:
        print("No data found.")

if __name__ == "__main__":
    report_rating()