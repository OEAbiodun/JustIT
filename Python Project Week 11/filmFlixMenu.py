import displayAllRecs, addFilm, update, delete, reports, reportAllFilms, reportParticularGenre, reportYearReleased, reportParticularRating, firstChar
# import displayAllRecs, addFilm, update, delete 
# from reports import *
# from connect import *
# from reportAllFilms import * 
# from reportParticularGenre import *
# from reportYearReleased import *
# from reportParticularRating import *


# create function 
def menuFile():
    with open('Python Project Week 11/filmFlixMenu.txt') as filmMenuFile:

        # read from the menu file and assign it to a variable
        filmFileData = filmMenuFile.read()

        return filmFileData
    
# print(menuFile())

def filmflixMenu():
    option = 0 # initialise the option variable with an integer value 0
    optionsList = ["1","2","3","4","5","6","7"]

    # initialise the menu file function with the choiceMenu variable 
    choiceMenu = menuFile() 

    while option not in optionsList:
        # call/invoke the function though the variable choiceMenu
        print(choiceMenu) # display the options from the menu file

        # re-assign the value of the option variable 
        option = input("Enter an option from the FilmFlix Main menu: ")
        # if user input is not on the list
        if option not in optionsList:
            # do this/execute the code below
            print(f"{option} is not a valid choice! ")
    return option
# print(songsMenu())

# create a boolean variable 
mainProgram = True

while mainProgram: # while True
    # initialise the songsMenu function with the choiceMenu mainSongsMenu 
    mainMenu = filmflixMenu()

# if the user input is string value 1
    if mainMenu == "1":
        addFilm.insert_films()

    elif mainMenu == "2":
        delete.delete_films()

    elif mainMenu == "3":
        update.update_films()
    
    elif mainMenu == "4":
        displayAllRecs.read_films()

    elif mainMenu == "5":
        firstChar.firstChar()

    elif mainMenu == "6":



        # reports.reports()
        def menuFile():
            with open('Python Project Week 11/reportMenu.txt') as filmMenuFile:

        # read from the menu file and assign it to a variable
                filmFileData = filmMenuFile.read()

            return filmFileData

        def filmflixMenu():
            option = 0 # initialise the option variable with an integer value 0
            optionsList = ["1","2","3","4", "5", "6"]

    # initialise the menu file function with the choiceMenu variable 
            choiceMenu = menuFile() 

            while option not in optionsList:
        # call/invoke the function though the variable choiceMenu
                print(choiceMenu) # display the options from the menu file

        # re-assign the value of the option variable 
                option = input("Enter an option from the FilmFlix Report menu: ")
        # if user input is not on the list
                if option not in optionsList:
            # do this/execute the code below
                    print(f"{option} is not a valid choice! ")
            return option
# print(songsMenu())

# create a boolean variable 
        mainProgram = True

        while mainProgram: # while True
    # initialise the songsMenu function with the choiceMenu mainSongsMenu 
            mainMenu = filmflixMenu()

# if the user input is string value 1
            if mainMenu == "1":
                reportAllFilms.report_films()

            elif mainMenu == "2":
                reportParticularGenre.report_genre()

            elif mainMenu == "3":
                reportYearReleased.report_yearRelease()
    
            elif mainMenu == "4":
                reportParticularRating.report_rating()

            elif mainMenu == "5":
                reports.reports()

            elif mainMenu == "6":
                print("Returning to the main menu")
                
                def menuFile():
                    with open('Python Project Week 11/filmFlixMenu.txt') as filmMenuFile:

        # read from the menu file and assign it to a variable
                        filmFileData = filmMenuFile.read()

                    return filmFileData
                break
            else:
                print("Invalid Choice")
        #         mainProgram = False



                def menuFile():
                    with open('Python Project Week 11/filmFlixMenu.txt') as filmMenuFile:

        # read from the menu file and assign it to a variable
                        filmFileData = filmMenuFile.read()

                    return filmFileData

        #         mainProgram = True           
    else:
    
        # reassign the boolean variable of 'mainProgram' False
        mainProgram = False
input("Press enter to quit FilmFlix App")