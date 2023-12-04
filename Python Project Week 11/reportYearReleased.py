from connect import *
from tabulate import tabulate

def report_yearRelease():

    yearReleased = input("Enter the Movie year: ")
    
    # dbCursor.execute("SELECT * FROM tblFilms WHERE Genre = {};".format(inputGenre))
    dbCursor.execute("SELECT * FROM tblFilms WHERE yearReleased = ?", (yearReleased, ))
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
    report_yearRelease()