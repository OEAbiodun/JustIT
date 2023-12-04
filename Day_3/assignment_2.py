# Debug and fix the multiplication program below 
# add comment where you fix the bugs

print("Welcome to the table quiz.\n")
num = int(input("Enter a number: "))


for i in range(1,11):
    answer = int(input(f" What is {i} x {num}? "))
    print(f"the answer is {answer} ")
    correct = i * num 
    if answer == correct:
        print("Correct")
    else:
        print(f"No, the answer is  {correct}")

print("Finished")