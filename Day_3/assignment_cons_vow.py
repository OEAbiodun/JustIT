word = str(input("Enter a word "))

vowels = ('a', 'e', 'i', 'o', 'u')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

for letter in word:
    if letter.lower() in vowels:
        print(letter, 'Is a vowel')
    elif letter in consonants:
        print(letter, 'is a consonant')
    else:
        print('This is not a valid input')