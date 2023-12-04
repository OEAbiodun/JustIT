import reportAllFilms, reportParticularGenre, displayAllRecs, reportYearReleased, reportParticularRating

# create function 
def reportMenuFile():
    with open('Python Project Week 11/reportMenu.txt') as reportMenuFile:

        # read from the menu file and assign it to a variable
        reportFileData = reportMenuFile.read()

        return reportFileData
    
# print(reportMenuFile())

def reportMenu():
    option = 0 # initialise the option variable with an integer value 0
    optionsList = ["1","2","3","4","5"]

    # initialise the menu file function with the choiceMenu variable 
    choiceMenu = reportMenuFile() 

    while option not in optionsList:
        # call/invoke the function though the variable choiceMenu
        print(choiceMenu) # display the options from the menu file

        # re-assign the value of the option variable 
        option = input("Enter an option from the reports Menu: ")
        # if user input is not on the list
        if option not in optionsList:
            # do this/execute the code below
            print(f"{option} is not a valid choice! ")
    return option
# print(reportMenuFile())

# create a boolean variable 
mainProgram = True

while mainProgram: # while True
    # initialise the songsMenu function with the choiceMenu mainSongsMenu 
    mainMenu = reportMenu()

# if the user input is string value 1
    if mainMenu == "1":
        reportAllFilms.report_films()

    elif mainMenu == "2":
        reportParticularGenre.report_genre()

    elif mainMenu == "3":
        reportYearReleased.report_yearRelease()
    
    elif mainMenu == "4":
        reportParticularRating.report_rating()

    else:
        # reassign the boolean variable of 'mainProgram' False
        mainProgram = False
input("Press enter to quit FilmFlix report. ")