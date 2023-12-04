from connect import *

def insert_songs():
    """Inserts songs into the database"""
    # SongId is auto increment 
    songTitle = input("Enter Song Title ")
    songArtist = input("Enter Song Artist ")
    songGenre = input("Enter Song Genre ")

    dbCursor.execute("INSERT INTO songs(Title, Artist, Genre) Values (?, ?, ?)", (songTitle, songArtist, songGenre))

    # Commit the change

    dbCon.commit()

    print(f"{songTitle} inserted into songs table ")
if __name__ == "__main__":
    insert_songs()



