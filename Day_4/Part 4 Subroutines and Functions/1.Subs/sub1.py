"""
Subroutine is a Sequence of instructions/code block to perform a specific task with an 
identifiable name.  A subroutine does not have a return statement
def keyword is used to define a subroutine, followed by the name of the subroutine
A subroutine is not executed unless it is invoked/called

"""
# syntax   def Keyword subroutineName():

# what is the similarity between function keyword in JS and def keyword in python?
# define a subroutine called userName
def userName():
    name = "Freddy"   #input("Please type your name: ") 
    print(name)

# call / invoke the subroutine
#userName()

# Exercise modify the code above in the subroutine to ask for user input
# instead of hard coded values






















def order():

    starter = input("What would like as your starter?")
    main = input("What would like as your main?")
    dessert = input("What would like as your dessert?")

    print(f'You have ordered:\n starter: {starter}\n main: {main}\n dessert: {dessert}')
  
#order()

def order1(starter, main, dessert):
   print(f'You have ordered:\n starter: {starter}\n main: {main}\n dessert: {dessert}')
  
#order1(input("What would like as your starter?"), input("What would like as your main?"), input("What would like as your dessert?"))

