print('******************* Welcome To My Choice *******************')
choice = input("""A: Music \nB: Maths \nC: English \nD: Science \nQ: Exit Program  """)

if choice == 'A' or choice == 'a':
    print('You have selected Music')
elif choice == 'B' or choice == 'b':
    print('You have selected Maths')
elif choice == 'C' or choice == 'c':
    print('You have selected English')
elif choice == 'D' or choice == 'd':
    print('You have selected Science')
elif choice == 'Q' or choice == 'q':
    Exit()
    print('You have selected to Exit')
    print('Are you sure you want to Exit?')
else:

    print("Invalid Option. Please Try Again.")

