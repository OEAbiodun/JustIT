def addition1(pNum1, pNum2, *args):

    answer = pNum1 + pNum2
    #(0,1,2,3,4,5)
    print(args)

    for value in args:
        print(value)

    return args


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

#print(addition1(num1, num2))
print(addition1(4, 5, "Name", "Fruit", "Drink", "4", "7.5", "True"))

"Modify the code above to use args(arguments)"






"""

# Use the argument to pass a number of number of values/parameter to a function/parameter
def addition2(*argNums):  #

    for nums in argNums: # nums = index, Tuple
        print(nums)

    answer = argNums[0] + argNums[1]
    print(answer)

addition2(1, 2, 3, 4, 5, 6, 7 ,8)








# If argNums was a list, what would be nums give me in order to 
# access the information in the list. # Index








addition2(1, 2, 3, 4, 5, 21, 45, 56, 78, 90, 1223, 56788, 6767)
print("Next function call\n")
addition2(1, 22)

print("Next function call\n")
addition2(1, 22, 45, 56)











"""
def user(*argDetails):  #

    print(argDetails[0])
    print(argDetails[1])
    print(argDetails[2])
    
customer =("Tim", "Jones", 30)
#customer =(Your Name, Your Surname, YourAge)

user(customer[0], customer[1], customer[2])
"""



# Use one parameter and the argument to pass one parameter and 
# a number of number values/parameter to a function/parameter










def addition(pArg1, *argNums):  #
    print(f"The first number: {pArg1}") #10

    for nums in argNums:
        print(f"The next number: {nums}") # 22, 45, 56


addition(10, 22, 45, 56)

"""








def item(para1, para2, *args):

    sum = para1 + para2
    # tuple ~(6,7,8,9,1)
    for number in args:
        print(number)
    return sum

result = item(4,5,6,7,8,9,1)