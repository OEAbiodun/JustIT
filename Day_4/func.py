def userName():
    name = input('Please, enter your name: ')
    print (f'Hello {name}, how are you today?')
userName()

def addtion():
    answer = 2 + 10
    print (f'The answer to 2 + 10 is {answer}')

addtion()

def cal():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2

    print (f'Answer to this multiplication is {result}')
cal()

def ran():
    numb1 = int(input("Enter the first number: "))
    numb2 = int(input("Enter the second number: "))

    res = numb1 / numb2
    print (f'Answer to this division is {res}')
ran()    

def sub():
    numb1 = int(input("Enter the first number: "))
    numb2 = int(input("Enter the second number: "))

    res = numb1 - numb2
    print (f'Answer to this subtraction is {res}')
sub() 