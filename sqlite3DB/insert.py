from connect1 import *

def insert_users():
    """Inserts songs into the database"""
    # SongId is auto increment 
    username = input("Enter Username ")
    Email = input("Enter Email ")

    dbCursor.execute("INSERT INTO users(username, Email) Values (?, ?)", (username, Email))

    # Commit the change

    dbCon.commit()

    print(f"{username} inserted into user table ")
if __name__ == "__main__":
    insert_users()
