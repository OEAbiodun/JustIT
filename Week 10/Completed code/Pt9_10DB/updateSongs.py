from connect import *

def update_songs():
    """
    This function updates the song list in the database.
    """
    idField = input("Enter the Song ID of the record you want to update: ")

    fieldName = input("Enter Title or Artist or Genre as field name: ").title()

    fieldValue = input(f"Enter the Value for {fieldName} field: ")
    "Method1"
    fieldValue = "'" + fieldValue + "'"

    # "Method 2"
    # tuple(fieldValue)
    # num = "2"
    # int(mum)

    dbCursor.execute(f"UPDATE songs SET {fieldName}  = {fieldValue} WHERE SongID = {idField} ")

    dbCon.commit()

    print(f"Record {idField} updated ")

if __name__ == "__main__":
    update_songs()

