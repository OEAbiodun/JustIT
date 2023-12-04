from connect import * 
from tabulate import tabulate


def reports():
    dbCursor.execute("SELECT filmID, title, yearReleased FROM tblFilms ORDER BY title DESC")
    # dbCursor.execute("SELECT * FROM tblFilms WHERE genre = 'PG' OR 'G'")
    dbCursor.execute("SELECT * FROM tblFilms WHERE rating = 'PG' OR 'R' OR 'G' OR 'U'")

    reportsDaa = dbCursor.fetchall()


    # for records in reportsDaa:
    #     print(records)


    if reportsDaa:
        headers = [i[0] for i in dbCursor.description]
        table = tabulate(reportsDaa, headers, tablefmt="grid")
        print(table)
    else:
        print("No data found.")

if __name__ == "__main__":
    reports()