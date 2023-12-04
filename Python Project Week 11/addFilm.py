from connect import *

def insert_films():
    """Inserts songs into the database"""
    # SongId is auto increment
    filmID = input("Enter Film ID: ") 
    filmTitle = input("Enter Film Title: ")
    filmYear = input("Enter Film Year: ")
    filmRating = input("Enter Film Rating: ")
    filmDuration = input("Enter Film Duration: ")
    filmGenre = input("Enter Film Genre: ")

    dbCursor.execute("INSERT INTO tblfilms(filmID, Title, YearReleased, Rating, Duration, Genre) Values (?, ?, ?, ?, ?, ?)", (filmID, filmTitle, filmYear, filmRating, filmDuration, filmGenre ))

    # Commit the change

    dbCon.commit()

    print(f"{filmTitle} inserted into films table. ")
if __name__ == "__main__":
    insert_films()



