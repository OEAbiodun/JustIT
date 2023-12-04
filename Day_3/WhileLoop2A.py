"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""


"""Comparison operator compare values
==    equal  ( 2 == 2)
< 	less than
> 	more than
<= 	less than or equal to 
>= 	greater than or equal to
!=    Not equal to"""

# While loop keeps looping/iterating until a condition is met
num = 1  # int(input("Enter number below 20: "))

while num <= 20: # while condition = True - then we keep looping
    print(f"The number is {num}")
    num += 1  # what is this doing ? increments num by 1 every loop

"Exercise: Modify the code above to countdown from 20"

# "solution"
print("\ncountdown from 20")
num = 20
while num >= 0:
    print(f"The number is {num}")
    num -= 1  # what is this doing ? decrements num by 1 every loop
