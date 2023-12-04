# import the datetime library/class/module
import datetime

print("Not using while Loop output")
dateTime = datetime.datetime.now()
print(dateTime.strftime("%H:%M:%S"))

# study the output of the code above and the output in the while loop to answer

# What is the while loop doing?

# add comment to explain what you understand the"datetime.datetime.now().strftime("%H:%M:%S")"

import time
# add comment to explain what you understand the 'end='
"""
Python's print() function comes with a parameter called 'end. 
By default, the value of this parameter is '\n', i.e. the new line character. 
"""

# add comment to explain what you understand the "\r""'
"""
The '\r' character is used to return the cursor to the beginning 
of the current line without advancing to the next line.
"""

print("while Loop output")
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
    time.sleep(1)
