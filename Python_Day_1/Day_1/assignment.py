list1 = [] # declare list1 variable and assign it a list datatype
list2 = ["HTML", "CSS"] 
print(list1)

list1.append("Bootcamp") # use append to add item to a list
print(list1) # index 0
list2.append("Bootcamp") # use append to add item to a list
print(list2) # index 2

# use the insert function to insert item to a specific index position
list2.insert(0, "Python") 
print(list2) # Python, HTML, CSS, Bootcamp

#access list items by their index position
#index    0        1       2     3  4   5     6     7
list3 = ["Paul", "Kate", "Anna", 1, 2, 34.7, -8 , "Katy"]
print(list3[1])

tuple1 = ("Paul", "Kate", "Anna", 1, 2, 34.7, -8 , "Katy")
# How do I access the data in this Tuple? print(tuple1[1])

#slicing a list 
print(list3[0:6:3]) #list[start:end] [START:END:STEP]

# return the length of the list
print("The length of the list is:", len(list3)) # use len function to return list length

# remove list items as per index position
print(list3)
del(list3[3]) # use del function to delete  by index position
del(list3[3], list3[5])
# del(list3[7])
print(list3)

# remove list items as per item value 
print(list3)
list3.remove("Kate") # use remove function to delete by item value
print(list3)

#max and min function
list4 = [ 1, 2, 34.7, -8 ]
# return the minimum item from the list
print(min(list4)) # -8

# return the maximum item from the list
print(max(list4))# 34.7

# sort list items
list4.sort() # sort list in ascending order
print(list4) #[-8, 1, 2, 34.7]

list4.sort(reverse=True)# sort list in descending order
print(list4) #[34.7, 2, 1, -8]

# clear list
list4.clear() # clear/ remove all list items
print(list4)

#Assignment 4

# ~list exercise
# create a list of 6 items
# insert a new item in postion 3
# add another item to the list
# remove an item by value
# remove the item at index position 3
# for every list manipulation print the list

myList = ['Hello', 'World', '!', 'Welcome', 'To', 'Python']
print(myList)

newItem = "Programming"
myList.insert(3, newItem)
print(myList)

myList.append('Javascript')
print(myList)

myList.remove('To')
print(myList)

del(myList[3])
print(myList)