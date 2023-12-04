# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
# https://docs.python.org/3/library/functions.html#zip

"""
List comprehensions provide a concise way to create lists. 
Common applications are to make new lists where each element is 
the result of some operations applied to each member of another 
sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
For example, assume we want to create a list of squares, like:
"""
print("squareNums1\n")
squareNums = []
for nums in range(5):
    squareNums.append(nums ** 2)
    print(squareNums)
print("squareNums1")
print(squareNums)
print("\n")

squareNums2 = [nums ** 2 for nums in range(6)]
print("squareNums2")
print(squareNums2)
print("\n")

"""
A list comprehension consists of brackets containing an expression followed by
a for clause, then zero or more for or if clauses. The result will be a new list
resulting from evaluating the expression in the context of the for and if clauses 
which follow it. For example, this listcomp combines the elements of two lists if they are not equal:

"""
# index =  0 1 2 3 4 .........
aList = [1, 2, 3, 4, 5]
bList = [6, 7, 8, 9, 10]
print(aList)
print(bList)

print(aList[2])
print(bList[4])


".................."
listAB = [(a, b) for a in aList for b in bList if a != b if a%2==0]
print(
    f"combined elements from listA {aList} and listB{bList}\nif the items are not the same\n{listAB}"
)


"................."
# joined lists

joinedList = aList + bList
print(f"The joined list\n{joinedList}")

# Slicing items  from two lists

slicedItems = aList[0:3] + bList[1:4]
print(f"Sliced List\n{slicedItems}")

# add values from list one list to another list
listAB = [aList[i] + bList[i] for i in range(len(aList))]
print(f"The Added items from list a {aList} and listb {bList}\n{listAB}")

# Find common list items
cList = [11, 20, 31, 4, 51, 9, 101]
dList = [
    6,
    71,
    81,
    9,
    101,
    20,
    31,
    4,
]
commonNums = [nums for nums in cList if nums in dList]
print(f"The commn list items are :\n{commonNums}")

commonNums.reverse()
print(commonNums, 'These items are printed in reverse order')
commonNums.sort()
print(commonNums, 'These items are printed in ascending order')

for nums in aList:
    if nums in bList:
        print(nums)

# Exercise: sort and print the items in the commons variable in ascending and descending order
# commonNums
# Exercise:  create two lists with at least two/three common names in both lists
# find the common names from both lists and put them in a commonNames List
# use the input and then the if to search the common names list for a specific name
# Exercise : Slice list aList from 0 - 5 and bList from 0 - 4 and put them together in a new list


# call a method on each element
freshfruit = ["  banana", "  loganberry ", "passion fruit  "]

print([weapon.strip() for weapon in freshfruit])



#create 2 list
list1 = ['Bread', 'Butter', 'Jam', 'Milk', 'Rice', 'Beans', 'Plantain', 'Egg']
list2 = ['Egg', 'Rice', 'Beans', 'Custard', 'Noodles', 'Garri', 'Spaghetti']
# list3 = [list1 + list2]
commonNames = []
# print (f'This is List 3', list3)

for i in list1:
    if i in list2:
        commonNames.append(i)
print('This is it', commonNames)
        # print ('Common Names between the two lists are ', commonNames)
        # print('These are the common names:', commonNames)

str = input('Enter Common Names to search: ').capitalize()

# for i in commonNames:
#     if i == str:
#         print(f'The common names between {list1} and {list2} are: ', commonNames)
#         print(f'{str} Found in the common names')
#         break
# else:
#     print(f'{str} Not Found!')
# print(commonNames)

if str in commonNames:
    print(f'{str.upper()} found in the common names of {list1} and {list2}')
else:
    print(f'{str.upper()} not found in the common names of {list1} and {list2}')


print ('Alist Slicing is: ', aList[0:5])
print ('Blist Slicing is: ', bList[0:4])

abList = [aList + bList]
print('Combined List is: ', abList)