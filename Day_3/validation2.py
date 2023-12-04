name = input("Enter name: ").title()

# Return True if the string is a lowercase string, False otherwise.
if name.istitle():
    print(f"Welcome {name}")
else:
    print(f"Your name {name} is not in title case")
    exit()  # exit
