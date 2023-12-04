from connect import *

def delete_films():
    # use primary key to update a record

    idField = input("Enter the Film ID of the record you want to delete: ")

    dbCursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idField}")
    # or
    # dbCursor.execute("DELETE FROM songs WHERE SongID=?", (idField,))
    dbCon.commit()

    print(f"{idField} has been deleted from the Films table")

if __name__ == "__main__":
    delete_films()