# def myname(firstName, LastName, Interest):
#     firstName = 'Olu'
#     lastName = 'Abi'
#     interest = 'Cooking'

#     print (f'Your First Name is: {firstName}\nYour last Name is: {LastName}\nYour Interest is: {Interest}')

# myname('firstName', 'LastName', 'Interest')

def myname(FirstName, LastName, Address, Interest):
    firstName = input('Enter you First Name: ')
    LastName = input('Enter you Last Name: ')
    Address = input('Enter Address: ')
    Interest = input('Enter you Interest: ')

    print (f'Your First Name is: {firstName}\nYour last Name is: {LastName}\nYour Address is: {Address}\nYour Interest is: {Interest}')

myname('FirstName', 'LastName', 'Interest', 'Address')