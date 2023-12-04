def ch():

  searchStr = "Python is a great programming language"
  findChar = input("Enter character to search for: ")


  for i in findChar:
    if i in searchStr:
      print(f'{findChar} is found in the search.')
    else:
      print(f'{findChar} is not found in the search.')

ch()
"iterate over a string to find an count a character"

# we set count to the value of zero

# loop through the entire string to search for the character entered

# check if the character entered is a match with any character in the string
# increase the count by 1 every time you find the same character

# display the result


# Exercise: refactor the code above by putting it into a subroutine and invoke it
