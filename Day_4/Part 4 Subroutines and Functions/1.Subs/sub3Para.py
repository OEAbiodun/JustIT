"""
In the subroutine definition, you pass in the parameter(placeholder)
In the subroutine call, you pass in the argument

# define subroutine fName with parameter, parameterFname
def fName(parameterFname):
    # pass the parameter inside the print statement
    print(f"My firstname is {parameterFname}")


"Method 1"
# in the subroutine call pass in the argument that will pass into the parameterFname
fName("Bob") # My firstname is Bob

"Method 2"
# use the input to ask for the value that will be saved in the argFirstname variable
argFirstname = input("What is your first name?:") #Tim
# in the subroutine call pass in the variable argFirstname as argument
fName(argFirstname) # My firstname is Tim

"Method 3"
fName(input("Enter your first name? "))  # the input is passed in as an argument

"""




# Exercise: Modify the code below to use parameters(arguments)
# define a subroutine called username
def username(first_name, last_name, interests): 
    print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests include: {interests}")
"""
    first_name = "Firstname"
    last_name = "last name"
    interests = "interests"
"""

username(input("Enter your first name?:"), input("Enter your last name?:"), input("Enter your interests?:"))
#            first name                  ,       last name                ,         interests
#username("Tim", "Jones", "Football")
# username(True, "Jones", [1,2,3,4,5])









"solution"
# define a subrouitine called userName
def userName(fullName, address, interest):
    print(f"my name is {fullName}, my address is {address} and my interest is {interest}")


"Method 1"
userName("Jane", "A234 THtd d", "Coding")

"Method 2"
# use the input to ask for the value that will be saved in the argFirstname variable
fullName = input("Enter your name: ")
address = input("Enter your address: ")
interest = input("Any interest? ")

userName(fullName, address, interest)

"Method 3"
userName(input("Enter your name: "), input("Enter your address: "), input("Any interest? ")) 
# the input is passed in as an argument







# Exercise: Modify the addition subroutine to use parameters
def addition(num1, num2):
    total = num1 + num2
    print(total)










"Method 1"
print("This is method 1\n")
addition(21, 34)  # pass in hardcoded values(numbers) as arguments


"Method 2"
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# The variables num1 and num2 are passed in as arguments 1 and 2 respectively
# The values held in the two variables(num1 and num2) will be passed into
# the parameters paraNum1 and ParaNum2
print("This is method 2\n")
addition(num1, num2)

"Method 3"
addition(int(input("Enter First Number:")), int(input("Enter Second Number:")))
