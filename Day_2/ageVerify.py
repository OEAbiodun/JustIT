from datetime import date

todayDate = date.today()

id = 'Yes'
DOB  = int(input("Please enter your Date Of Birth."))
currentYear = todayDate.year

age = (int(currentYear) - int(DOB))
print (f"You are", {age}, "years old.")

if age >= 18:
    print ("You are Old enough to buy Alcohol.")
    
    userID = input('Do you have an ID?')
    if userID == 'Yes' or userID == 'YES' or userID == 'yes':
        print ('Great! You can go out and enjoy the nightlife.')
    else:
        print('You need an ID as a proof of your age.')

else:
    print('You are too young to buy an Alcohol')