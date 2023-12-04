def addition():
    answer = 2 + 10
    print(f"The answer to  2  + 10 is {answer} ")
 
# addition()  # call / invoke the subroutine
# Exercise: 
#Modify the code above to use variables for the numbers 
#added with the input function



# Exercise: Modify the code above by changing subroutine name to 
# subtraction, multiply or divison to perform the respective operations
"""






# def keyword followed by the name/identifier 
def plus():

    # code block that is to run, when subroutine is called
    sum = int(input("Enter Value One:")) + int(input("Enter Value Two:"))

    # make sure to print the value as we have no return statement
    print(sum)

# calling/invoking the subroutine    
plus()
"""







def addition1():
    num1 = int(input("Please Enter First number: "))
    num2 = int(input("Enter second number: "))
    print(f"The answer to {num1} + {num2} is {num1 + num2}") # ***


def multiply():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = num1 * num2
    print(f"The answer to {num1} x {num2} is {answer}")

def divide():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = num1 / num2
    print(f"The answer to {num1} / {num2} is {answer}")
    
def subtract():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = num1 - num2
    print(f"The answer to {num1} - {num2} is {answer}")