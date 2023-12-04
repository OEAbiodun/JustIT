# Exercise: modify the subroutine below as a function.
# For an added challenge make the code as concise as possible
def userName4():  # define a subrouitine called userName
    fullName = input("Enter your name: ")
    address = input("Enter your address: ")
    interest = input("Any interest? ")
    print(f"my name is {fullName}, my address is {address} and my interest is {interest}")














#solution:
def username1(fullName, address, interest):
    return (fullName, address, interest)
    # return makes this a function - subroutine does not have the return statement

profile = username1(input("Enter your name: "), input("Enter your address: "),input("Any interest? "))
print(profile)
print(f"my name is {profile[0]}, my address is {profile[1]} and my interest is {profile[2]}")

if profile[1] == "London":
    print("You live in London")

for item in profile:
    print(item)

starters ={1:"melon", 2:"prawns"}
mains ={}
dessert ={}

print("please give the option number for your starter: \n1. Melon \n2.Prawns")
userOption1 = int(input("Starter Choice:"))











def userName():
    text = f"my name is {input('Enter your name: ')}, my address is {input('Enter your address: ')} and my interest is {input('Any interest? ')}"
    return text









def userName1(fullname, address, interest):
    print(f"my name is {fullname}, my address is {address} and my interest is {interest}")
    return


"""Method 1"""

userName1("Tim", "HJ9 7GH", "Coding")


"""Method 2"""
name = input("What is your name?")
postcode = input("What is your postcode?")
hobby= input("What is your hobby?")

userName1(name,postcode,hobby)

"""Method 3"""
userName1(input("What is your name?"),input("What is your postcode?"),input("What is your hobby?"))


































"Solution"

# exercise :modify the code below and put it into a function with parameters

fName = input("What is your first name? ")
lName = input("What is your last name? ")
interest = input("Do you have any interests? ")

def username(first_name, last_name, interests):  # define a subroutine called username
    return print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests include: {interests}")

username(fName,lName,interest)