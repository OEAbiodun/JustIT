# Use the keyword argument where you provide a name to the variable 
# as you pass it into the function
# Think of kwargs as being a dictionary

def addition1(**kwargs):  #KeyWord ARGumentS

    for varKeys, numsValue in kwargs.items(): # an item is one pair
        print(varKeys, numsValue)
# {key:value, }

addition1(num1=10, num2=20, num3=30) 

def addition2(**kwargs):  #

    for varKeys in kwargs.keys(): # filter by key name only
        print(f"The keys {varKeys}")

addition2(num1=10, num2=20, num3=30)

def addition3(**kwargs):  #

    for numsValue in kwargs.values(): # filter by value
        print(f"Value {numsValue}")

addition3(num1=10, num2=20, num3=30)

# dictionary1 = {"name":"Tim", 1:"Apple"}

# print(dictionary1)
# print(dictionary1[])


def userDetails(pfName, pAddress, pInterest, **kwargs):

    # userDetails = f"Your name is {pfName}, and you live at {pAddress}, and your inteest is {pInterest}"
    # return userDetails
    print(
        f"Your name is {pfName}, and you live at {pAddress}, and your inteest is {pInterest}"
    )

    for keyNums, value in kwargs.items():
        print(f"The key is {keyNums} ! Value {value}")


userDetails("Em", "123 No Way", "Coding", num1=10, num2=20, num3=30)
# .items() = each dictionary item, .keys() = each key, .values() = each value
