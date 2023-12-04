from connect import *

def update_films():
    """
    This function updates the song list in the database.
    """
    idField = input("Enter the Film ID of the record you want to update: ")

    fieldName = input("Enter FilmID, Title, YearReleased, Rating, Duration, Genre as field name: ").title()

    fieldValue = input(f"Enter the Value for {fieldName} field: ")
    "Method1"
    fieldValue = "'" + fieldValue + "'"

    dbCursor.execute(f"UPDATE tblfilms SET {fieldName}  = {fieldValue} WHERE FilmID = {idField} ")

    dbCon.commit()

    print(f"Record {idField} updated ")

if __name__ == "__main__":
    update_films()

