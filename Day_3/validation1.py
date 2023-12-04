try:  # the code to try and execute
    num1 = input("Enter first number: ") #one
    num2 = input("Enter second number: ") #1
    total = int(num1) + int(num2)
    print(total)

except Exception as e:  # handle the error
    print(f"The following error has occurred: {e}")

"""
 #Single Error Handling
except ValueError:  # handle the error
    print(f"Please Enter a numeric value")
    # run function

print("Some process to execute")
print("Some process to execute")
print("Some process to execute")
print("Some process to execute")
print("Some process to execute")
"""


"""
#Multiple Error Handling
except (ValueError, IndexError, NameError) as e:  # handle the error

    if ValueError:
        print(f"Please Enter a numeric value")
    elif IndexError:
        print(f"The following error has occurred: {e}")
    else:
        print(f"The following error has occurred: {e}")


#Generic Error Handling
except Exception as e:  # handle the error
    print(f"The following error has occurred: {e}")
"""
print("Some process to execute")
print("Some process to execute")
print("Some process to execute")
print("Some process to execute")
print("Some process to execute")
