"""You can perform operations with string in a similar way to the operations 
that you can perform with numbers. """

a = int(input("Please enter a Number: "))
b = int(input("Please enter a Number: "))

if (a > b):
#compareLetters = "a" > "b"  # check if the letter a is greater than b
    print(f'{a} is greater than {b}')
else:
    print(f'{b} is greater than {a}')


letterA = input('Enter first word: ')
letterB = input('Enter second word: ')
if letterA > letterB:
    print(f'{letterA} comes after {letterB}')
elif letterA < letterB:
    print(f'{letterB} comes before {letterA}')
else:
    print('The words are equal')


town= "York"
city = "york"
print(town == city) #False, Capital letter - ASCII Table 

compareLetters = "b" > "a"  # check if the letter b is greater than a
print(compareLetters)

"You can multiply a string, it will concatenate the same value for the number of times stated."
mutiplyWord = "Python\n" * 5  # mulitply the word n times
print(mutiplyWord) #TimTimTimTimTim

"""The + sign concatenates (joins) the two string together.
There is no space because it hasn't been given that instruction"""
joinWords = "Python" + " " + "Java"  # join the two words
print(joinWords)
"Exercise"
# Create two variables fName and lName and join and print them using a variable called fullName

"You can also use string-handling techniques to find out things about a string.  "
"""
len() is used to count the number of characters in a string.
This would include spaces as well if they were present.
In Python, the index always starts at 0.

# """
course = "Python"
wordlength = len(course) #6
print(wordlength)  # returns the length of the string

# How can we find/print a specific character in a word or string in a list?
# "Python"[0]
findFirstLetter = course[0]  # returns the first character from the string "Python"
print(findFirstLetter)

"Exercise"
# Return all the characters from the string held in the course variable using negative values

# [-6:] [0:]

# How can you access the letter h?

"Exercise:"
#  use any comparison operator to compare the letter "a" and "A"
#  use any comparison operator to compare the letters "ax" and "ZZ"
#  use any comparison operator to compare your firstname with any another first name
# != , == , <= , >=, <,>

"For further reading See Python documentation for other string methods"
# https://docs.python.org/3.3/library/stdtypes.html?highlight=substring#string-methods
"""swapcase()
capitalize()
endswith()
find() 
isnumeric()
isdigit()
isdecimal()
"""

"""
programme = "Match of the Day"
#            0123456789 h[10] e[11] space[12] D[13] a[14] y[15]
# 
print(programme[0]) #M
print(programme[-1]) #y
print(programme[-9]) #f
print(programme[-9:]) #[start:end], f the Day
print(programme[-16:]) #[start:end], Match of the Day
"""




