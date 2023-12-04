"""
function is a Sequence of instructions/code block to perform a specific task with 
an identifiable name
A function must have a return statement
def keyword is used to define a function, followed by the name of the function
A function is not executed unless it is invoked/called

"""
def addition():
    num1 = int(input("Enter first number: ")) # value inputted and stored in num1 #2
    num2 = int(input("Enter second number: ")) # value inputted and stored in num2 #3
    answer = num1 + num2 # num1 and num2 values added and answer stores the value
    return (answer, num1, num2) # return stops the function running and outputs to value held in answer

sum = addition() #5
print(sum)
calc = sum * 50 # 5 * 50

"Method 1"
print(f"The answer is {addition()}")

"Method 2"
myAddition = addition()
print(f"The answer is {myAddition}")

addition()