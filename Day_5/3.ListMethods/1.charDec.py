"Use chr() and ord() to perform ASCII conversions"

# Performing ASCII conversions in Python​
# Python has two functions that perform ASCII conversions: ​
# chr(97):This takes a decimal number and returns its character equivalent. ​
# ord("a"):This takes a character and returns its decimal equivalent. ​


aChar = input("Enter a character: ")
# ord takes a character and returns its decimal equivalent
convertChar = ord(aChar)
print(convertChar)


userMsg = "Message"
number = int(input("Enter number: "))
convertNum = chr(number)
secretMsg = userMsg + convertNum
print(secretMsg)


# chr(97):This takes a decimal number and returns its character equivalent. ​

"""Exercise: Complete the code block below to print a list of converted numbers to letter as specified in the range, the 
questions marks indicates where the code is missing"""
# def alphabets(): # created the function alphabets
#     alphabetList = ? # create an empty list
#     for ? in range(65, 123):
#         alphabetList.append(chr(letters))  # converts numbers to letters
#     return ?


# print(?)
