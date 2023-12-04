from connect import *
from tabulate import tabulate

def read_films():
    
    dbCursor.execute("SELECT * FROM tblfilms")
    allRecords = dbCursor.fetchall()

    # for eachRecords in allRecords:
    #     print(eachRecords)

    if allRecords:
        headers = [i[0] for i in dbCursor.description]
        table = tabulate(allRecords, headers, tablefmt="grid")
        # print("Total number of rows in table: ", dbCursor.rowcount)
        print(table)
    else:
        print("No data found.")

if __name__ == "__main__":
    read_films()