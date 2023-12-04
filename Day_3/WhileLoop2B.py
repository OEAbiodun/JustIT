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

userNum = int(input("Enter a number: ")) #8
while num <= 20:
    print(f"The number is {num}")

    if num == userNum:  # set the condition to exit the loop
        print("exiting the loop...")

        break

    num += 1  # what is this doing ?

print("we have broken the loop")
