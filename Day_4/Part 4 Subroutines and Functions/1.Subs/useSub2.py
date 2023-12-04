from sub1 import *  # imported everythin from sub1 module/lib

# from sub2 import addition,divide,multiply,subtraction
"Same as import * below"
from sub2 import addition, divide, multiply, subtract # addition,divide,multiply,subtraction
from time import sleep
 
# Make the subroutine call username from the sub1 python application
userName()

sleep(5)  # wait/delay for 5 seconds
# print("Welcome to the QA app, please answer the questions below truthfully\n")
multiply()
print("Please answer the Multiplication questions below\n")


sleep(3)
addition()
print("Please answer the Addition questions below\n")


sleep(3)
subtract()
print("Please answer the Subtraction questions below\n")


sleep(3)
divide()
print("Please answer the Division questions below\n")
