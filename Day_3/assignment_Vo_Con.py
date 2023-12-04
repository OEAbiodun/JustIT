vowels = ('a', 'e', 'i', 'o', 'u')
word = input("Please, Enter a Word: ")

for i in word:
    if i in vowels:
        print(f"{i} Is a vowel." )
else:
    print(f"{i} Is a consonant.")