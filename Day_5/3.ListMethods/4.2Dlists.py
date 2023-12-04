"List methods"
"list.append(item)"  # add item at end of list
"list.insert(index,item)"  # add item at index
"list.pop(index)"  # remove item at index
"list.remove(item)"  # remove item
"list.index(item)"  # search for index of item
"list.count(item)"  # get occurrences of item
"list.reverse()"  # reverse list
"list.sort()"  # sort list

"Traverse"  # Move through a sequence.
"Method"  # A function that belongs to an object.
"Custom  built function"  # A function that you have created yourself and imported into other programs that you have created.
"List"  # A dynamic data structure that holds items under one name. The items can be of varying data types.


# The list below contains string literals (i.e. pieces of text) and need to be in quotes
listOfNames = ["Nicole", "Laura", "Silvia", "Steve", "Juliet"]
for index in range(len(listOfNames)):
    print(f"{index} : {listOfNames[index]}")

print(f"\n{listOfNames}")
# What item is returned from the list and why?
print(f"{listOfNames[2]}\n")

"Exercise:"
# You have been provided with the multidimentional list below.
"Your tasks are listed below"
# 1. Print the multidimentional list
# 2. Print Nicole, number 10 and JS
# 3. Print Laura, number 20 and Python
# 4. Print Juliet, number 50 and NoSQl


twoDLists = [
    #      0      1          2       3       4
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],  # 0
    # List of numbers
    [10, 20, 30, 40, 50],  # 1
    # List of Tecnologies
    ["JS", "Python", "HTML", "CSS", "NoSQL"],  # 2
]

"Reasearch Nested for loop"
print("Nested for loop..........")
# Can you use a nested for loop to loop through the multidimensional list ?

"Reasearch enumerate"
print("Nested for loop with enumerate..........")
# Can you use a nested for loop and enumerate through the multidimensional list?

# The enumerate object yields pairs containing a count
# (from start, which defaults to zero) and a value yielded by the iterable argument.


"Practice exercise over the weekend"
# Create a shopping list program
