# Use the keyword/named argument where you provide a name to the variable as you pass it into the function
# Think of kwargs as been a dictionary
# args accepts any number of positional argument


"Using  kwargs and Args "


def kwargsArgs(*args, **kwargs):

    # userDetails = f"Your name is {pfName}, and you live at {pAddress}, and your inteest is {pInterest}"
    # return userDetails
    print(f"The args {args}")
    print(f"The kwargs {kwargs}")
    print("Finished unpacking argKwarg\n")


kwargsArgs(
    "Em",
    "123 No Way",
    "Coding",
    "happy",
    "gaming",
    "Python",
    "java",
    num1=1,
    num2=2,
    num3=3,
    num4=10,
)

kwargsArgs(
    num1=1,
    num2=2,
    num3=3,
    num4=10
    )

kwargsArgs(
    "Em",
    "123 No Way",
    "Coding",
    "happy",
    "gaming",
    "Python",
    "java"
    )

dict = {"a": "123", "b": "456", "c": "789"}
string = "123"
print(string.maketrans(dict))