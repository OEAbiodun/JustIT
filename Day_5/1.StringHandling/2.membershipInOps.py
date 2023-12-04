"The for loop can be used to iterate through a string and any sequence of elements(eg numbers etc)"

name = "Tim is Software Technical Trainer"
for letter in name:
    print(letter)


searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ") #i

"""The membership operator can be used to check if a value/substring is present 
or not in object and returns true if it does"""
if findChar in searchStr:  # opposite of the in operator is the 'not in'
    print(f"Found {findChar}")
else:
    print(f" Not Found")

"Exercise: replace the in operator with the 'not in' operator "
if findChar not in searchStr:  # opposite of the in operator is the 'not in'
    print(f"Found {findChar}")
else:
    print(f" Not Found")


# Further reading on operators not covered in the bootcamp see links below
"https://www.w3schools.com/python/gloss_python_identity_operators.asp"
"https://www.w3schools.com/python/gloss_python_bitwise_operators.asp"

"Exercise:"
# You have been provided with the vowels in a list data structure and a variable
# name that is assigned with an empty string.

"Your task is to assign your name to the variable called name and use a for loop and if statement to:"
"Iterate through the list of vowels to find the vowels in your name"

vowels = ["a", "e", "i", "o", "u"]  # vowels
name = "Oluwaseun"  # Add your name in between the speech marks

for j in range(len(vowels)):
    if vowels[j] in name.lower():
        print(f"{vowels[j]} is in {name}")


def sub1():
    print("Hello World")














"solution 1"
for x in range(len(vowels)):
    if vowels[x] in name:
        print(f"The vowel {vowels[x] } found")
    else:
        print(f"The vowel {vowels[x] } not found")

"solution 2"
for i in name:
    if i in vowels:
        print(f"I found the vowel {i} in your name.")
    else:
        print(f"The vowel {i} not found")
